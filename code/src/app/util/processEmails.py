
import os
from win32com.client import Dispatch
import pandas as pd
import extract_msg
import re
import shutil
from bs4 import BeautifulSoup
import os
import mailparser
from email import message_from_file
import base64
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import fitz
from pathlib import Path
import pdfplumber

def clean_filename(filename):
    return re.sub(r'[\x00-\x1F<>:"/\\|?*]', '', filename)

def readfromWord1(filepath):
    from docx import Document

    try:
        doc = Document(filepath)
        text = "\n".join(para.text.strip() for para in doc.paragraphs if para.text.strip())
        return text
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def readfromWorddoc1(filepath, output_path=None):
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

def parse_pdf_email(text):
    print(text)
    lines = text.splitlines()
    print(lines)
    sender, subject, body = "", "", ""

    for line in lines:
        print(line)
        if line.lower().startswith("from:") or line.lower().startswith("from ") :
            sender = line[5:].strip()
        elif line.lower().startswith("subject:") or line.lower().startswith("subject "):
            subject = line[8:].strip()
        else:
            body_index = lines.index(line) + 1
            body = "\n".join(lines[body_index:]).strip()
            break

    # Fallback if parsing fails
    if not sender:
        sender = "Unknown Sender"
    if not subject:
        subject = "No Subject"
    if not body:
        body = text

    return sender, subject, body

def extract_emails_and_attachments(folder_path, PropcessingFolderPath, EmailHeaderTemplate, dataFrameFolderName, emailHeaderDataSet,tesseract_cmd_path):
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd_path
    df = pd.DataFrame(columns=EmailHeaderTemplate)
    primary_key = 1

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        extension = Path(file_path).suffix.lower()
        text = ""  # Initialize text for every file

        try:
            # Handling .msg files
            if extension == ".msg":
                msg = extract_msg.Message(file_path)
                sender = msg.sender
                subject = msg.subject

                if msg.htmlBody:
                    soup = BeautifulSoup(msg.htmlBody, "html.parser")
                    body = soup.get_text()
                elif msg.rtfBody:
                    body = msg.rtfBody
                elif msg.body:
                    body = msg.body
                else:
                    body = ""

                attachment_names = []
                if msg.attachments:
                    attachment_folder = os.path.join(PropcessingFolderPath, f"Email_{primary_key}_Attachments")
                    os.makedirs(attachment_folder, exist_ok=True)

                    for attachment in msg.attachments:
                        clean_name = clean_filename(attachment.longFilename)
                        attachment_path = os.path.join(attachment_folder, clean_name)
                        attachment.save(customPath=attachment_folder)
                        attachment_names.append(clean_name)

            # Handling .eml files
            elif extension == ".eml":
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    msg = mailparser.parse_from_file(file_path)

                sender = msg.from_[0][1] if msg.from_ else ""
                subject = msg.subject if msg.subject else ""

                if msg.text_html:
                    soup = BeautifulSoup(msg.text_html[0], "html.parser")
                    body = soup.get_text()
                elif msg.text_plain:
                    body = "\n".join(msg.text_plain)
                else:
                    body = ""

                attachment_names = []
                if msg.attachments:
                    attachment_folder = os.path.join(PropcessingFolderPath, f"Email_{primary_key}_Attachments")
                    os.makedirs(attachment_folder, exist_ok=True)

                    for attachment in msg.attachments:
                        clean_name = clean_filename(attachment["filename"])
                        attachment_path = os.path.join(attachment_folder, clean_name)
                        with open(attachment_path, "wb") as f:
                            f.write(base64.b64decode(attachment["payload"]))
                        attachment_names.append(clean_name)

            # Handling .pdf files
            elif extension == ".pdf":
                with pdfplumber.open(file_path) as pdf:
                    for page in pdf.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n"

                # If no text is found, try OCR
                if not text.strip():
                    # Use PyMuPDF to convert PDF pages to images
                    doc = fitz.open(file_path)
                    for page_num in range(len(doc)):
                        page = doc.load_page(page_num)
                        pix = page.get_pixmap()  # Render page as an image
                        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                        # Perform OCR on the image
                        ocr_text = pytesseract.image_to_string(img)
                        text += ocr_text + "\n"

                sender = ""
                subject = file_name
                body = text.strip()
                attachment_names = []


            elif extension == ".doc":
                text= readfromWorddoc1(file_path)
                sender = ""
                subject = file_name
                body = text.strip()
                attachment_names = []

            elif extension == ".docx":
                text= readfromWord1(file_path)
                sender = ""
                subject = file_name
                body = text.strip()
                attachment_names = []

            else:
                # Skip files with unsupported extensions
                continue

            # Append extracted data to DataFrame after processing
            df.loc[len(df)] = [primary_key, sender, body, subject, "--".join(attachment_names),file_name]
            primary_key += 1

        except Exception as e:
            print(f"Error processing {file_name}: {e}")
            continue

    # Save DataFrame to CSV
    os.makedirs(dataFrameFolderName, exist_ok=True)
    df.to_csv(f"{dataFrameFolderName}/{emailHeaderDataSet}", index=False)



