# -*- coding: utf-8 -*-

import pdfplumber
from docx import Document
import win32com.client
import os
import pandas as pd
from PIL import Image
import pytesseract
from pathlib import Path

def readfrompdf(filepath):
    try:
        from PyPDF2 import PdfReader

        with open(filepath, "rb") as file:
            reader = PdfReader(file)
            text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()

            if not text.strip():
                doc = fitz.open(file_path)
                for page_num in range(len(doc)):
                    page = doc.load_page(page_num)
                    pix = page.get_pixmap()  # Render page as an image
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                    ocr_text = pytesseract.image_to_string(img)
                    text += ocr_text + "\n"

        return text
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def readfromWord(filepath):
    from docx import Document

    try:
        doc = Document(filepath)
        text = "\n".join(para.text.strip() for para in doc.paragraphs if para.text.strip())
        return text
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def readfromWorddoc(filepath, output_path=None):
    filepath = os.path.abspath(filepath)

    # Check if file exists
    if not os.path.exists(filepath):
        return f"Error: File not found at '{filepath}'"


    # Check if it's a .doc file
    if not filepath.lower().endswith(".doc"):
        return "Error: File is not a .doc format."
        return

    # Set output path if not provided
    if not output_path:
        output_path = filepath.replace(".doc", ".docx")

    try:
        # Open Word application in the background
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False  # Run in background

        # Open the .doc file
        doc = word.Documents.Open(filepath)

        # Save as .docx (FileFormat=16)
        doc.SaveAs(output_path, FileFormat=16)
        doc.Close()
        word.Quit()

        # Read text from the .docx file
        text = readfromWord(output_path)

        # Remove temporary .docx file
        try:
            os.remove(output_path)
        except OSError as e:
            print(f"Warning: Could not delete temporary file - {e}")

        return text

    except Exception as e:
        return "An error occurred: {e}"
        return None

def readfromText(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read().strip()
        return text
    except FileNotFoundError:
        return "Error: File not found."
    except PermissionError:
        return "Error: Permission denied. Cannot read the file."
    except Exception as e:
        return f"An error occurred: {e}"

def readfromExcel(filepath):
    try:
        import pandas as pd

        # Read Excel file
        df = pd.read_excel(filepath)

        # Convert DataFrame to string (no index)
        text = df.to_string(index=False)
        return text

    except FileNotFoundError:
        return "Error: File not found."
    except ValueError:
        return "Error: File format is not supported or corrupted."
    except Exception as e:
        return f"An error occurred: {e}"

def readfromCSV(filepath):
    try:
        df = pd.read_csv(filepath)
        text = df.to_string(index=False)
        return text
    except FileNotFoundError:
        return "Error: File not found."
    except pd.errors.EmptyDataError:
        return "Error: The file is empty."
    except pd.errors.ParserError:
        return "Error: Unable to parse the CSV file. It might be corrupted."
    except PermissionError:
        return "Error: Permission denied. Cannot read the file."
    except Exception as e:
        return f"An error occurred: {e}"

def readfromImage(filepath):
    try:
        img = Image.open(filepath)
        text = pytesseract.image_to_string(img)
        return text
    except FileNotFoundError:
        return "Error: File not found."
    except OSError:
        return "Error: Unsupported file format or corrupted image."
    except Exception as e:
        return f"An error occurred: {e}"

def unknown_file_type(file_path):
    return "nothing"

def ProcessAttachments(tesseract_cmd_path,dataFrameFolderName,emailHeaderDataSet,EmailAttachmentTemplate,PropcessingFolderPath,emailAttachmentDataSet):
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd_path
    extension_handlers = {
    '.pdf': readfrompdf,
    '.docx': readfromWord,
    '.txt': readfromText,
    '.csv' : readfromCSV,
    '.jpg': readfromImage,
    '.jpeg': readfromImage,
    '.png': readfromImage,
    '.xlsx': readfromExcel,
    '.doc' : readfromWorddoc,
    '.xls' : readfromExcel
    }

    df = pd.read_csv(f"{dataFrameFolderName}/{emailHeaderDataSet}")
    attachment_df = pd.DataFrame(columns=EmailAttachmentTemplate)
    for index, row in df.iterrows():
        id = row['Id']
        attachments = row['Attachments']
        attachment_list = [att.strip() for att in str(attachments).split('--')] if pd.notna(attachments) and str(attachments).strip() else []
        attachmentId = 1
        for attachment in attachment_list:
            file_path = os.path.join(f"{PropcessingFolderPath}\Email_{id}_Attachments", attachment)
            extension = Path(file_path).suffix.lower()
            handler = extension_handlers.get(extension, unknown_file_type)
            text = handler(file_path)
            attachment_df.loc[len(attachment_df)] = [id, attachmentId, attachment,text]
            attachmentId += 1
    attachment_df.to_csv(f"{dataFrameFolderName}/{emailAttachmentDataSet}", index=False)