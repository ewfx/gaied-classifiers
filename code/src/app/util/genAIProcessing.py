import json
import pandas as pd
import google.generativeai as genai
import re
from concurrent.futures import ThreadPoolExecutor


def prepareEmailData(dataFrameFolderName, emailHeaderDataSet, emailAttachmentDataSet, apiKey, GenAIModelName):
    # Read CSVs with proper encoding and error handling
    email_df = pd.read_csv(f"{dataFrameFolderName}/{emailHeaderDataSet}")
    attachment_df = pd.read_csv(f"{dataFrameFolderName}/{emailAttachmentDataSet}")

    # Merge on Id and MailId, left join ensures all emails are included, even without attachments
    merged_df = pd.merge(email_df, attachment_df, left_on="Id", right_on="MailId", how="left").fillna("")

    # Group and aggregate attachments, ensuring missing values are handled properly
    result = (
        merged_df.groupby(["Id", "Body", "Sender", "Subject","EmailFileName"])
        .agg({
            "FileName": lambda x: [
                {
                    "AttachmentId": merged_df.loc[i, "AttachmentID"] if pd.notna(merged_df.loc[i, "AttachmentID"]) else "",
                    "FileName": merged_df.loc[i, "FileName"] if pd.notna(merged_df.loc[i, "FileName"]) else "",
                    "Text": merged_df.loc[i, "Text"] if pd.notna(merged_df.loc[i, "Text"]) else ""
                }
                for i in x.index
            ]
        })
        .reset_index()
    )

    # Create combined JSON with Sender and Subject, ensuring missing attachments are represented as empty lists
    combined_json = result.apply(
        lambda row: {
            "Id": row["Id"],
            "Sender": row["Sender"],
            "Subject": row["Subject"],
            "EmailFileName": row["EmailFileName"],            
        },
        axis=1,
    ).to_json(orient="records")

    # Call the GenAI API and update original data with classification
    updated_json = []
    for item in json.loads(combined_json):
        result = callGenAI(item, apiKey,GenAIModelName)
        item.update(result)  # Add classification results to the original item
        updated_json.append(item)

    df = pd.DataFrame(updated_json)    
    return df

def load_prompt():
    """Loads the base prompt from the external prompt.txt file."""
    with open("app/prompt.txt", "r") as file:
        base_prompt = file.read()

    # Load and format categories from Excel
    category_dict = load_categories("app/categories.xlsx")
    formatted_categories = format_categories_for_prompt(category_dict)

    # Inject formatted categories into the base prompt
    prompt_with_categories = base_prompt.replace("{categories_placeholder}", formatted_categories)
    
    return prompt_with_categories

def load_categories(file_path="app/categories.xlsx"):
    """Reads categories from an Excel file and formats them for prompt injection."""
    category_df = pd.read_excel(file_path)

    # Grouping by RequestType and preparing category dictionary
    category_dict = {}
    for req_type, group in category_df.groupby("RequestType"):
        category_dict[req_type] = group["SubRequestType"].tolist()
    
    return category_dict

def format_categories_for_prompt(category_dict):
    """Formats categories as readable bullet points for the prompt."""
    formatted_text = ""
    for req_type, sub_types in category_dict.items():
        formatted_text += f"- **{req_type}:** Includes {', '.join(sub_types)}.\n"
    return formatted_text.strip()


def callGenAI(email_data, apiKey, GenAIModelName):
    # Configure API key for Gemini
    genai.configure(api_key=apiKey)

    # Initialize the model
    model = genai.GenerativeModel(GenAIModelName)

    # Load and format the dynamic prompt with categories
    base_prompt = load_prompt()
    prompt_text = base_prompt.replace("{json_data}", json.dumps(email_data, indent=2))

    try:
        # Call the Gemini model
        response = model.generate_content(prompt_text)

        # Extract and format the response correctly
        result = response.text.strip()

        # Clean up response if wrapped in code block
        if result.startswith("```json"):
            result = result.replace("```json", "").replace("```", "").strip()

        # Extract valid JSON if non-JSON text is included
        result = clean_json_response(result)

        # Parse the result to ensure valid JSON
        classified_result = json.loads(result)

        return classified_result

    except Exception as e:
        print(f"Error: Invalid or incomplete JSON response. Details: {e}")
        print(f"Raw response: {result}")
        return {}



def clean_json_response(raw_response):
    """
    Extracts valid JSON from API responses by removing non-JSON text.
    """
    match = re.search(r"\{.*\}", raw_response, re.DOTALL)
    if match:
        return match.group(0)
    else:
        raise ValueError("No valid JSON found in response.")

