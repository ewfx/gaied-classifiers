# process.py
import time
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.global_vars import (
    ProcessingFolderPath,
    dataFrameFolderName,
    EmailsFolderPath,
    emailHeaderDataSet,
    emailAttachmentDataSet,
    EmailHeaderTemplate,
    EmailAttachmentTemplate,
    MsgExtension
)
from config import tesseract_cmd_path,apiKey,GenAIModelName
from app.util.processEmails import extract_emails_and_attachments
from app.util.workspaceSetup import setupWorkspace
from app.util.extractTextFromAttchment import ProcessAttachments
from app.util.genAIProcessing import prepareEmailData



print('Processing started...')
setupWorkspace(ProcessingFolderPath,dataFrameFolderName)
extract_emails_and_attachments(EmailsFolderPath, ProcessingFolderPath,EmailHeaderTemplate,dataFrameFolderName,emailHeaderDataSet,tesseract_cmd_path)
ProcessAttachments(tesseract_cmd_path,dataFrameFolderName,emailHeaderDataSet,EmailAttachmentTemplate,ProcessingFolderPath,emailAttachmentDataSet)
df = prepareEmailData(dataFrameFolderName, emailHeaderDataSet, emailAttachmentDataSet, apiKey,GenAIModelName)
# Save the DataFrame as a CSV file
output_path = f"{dataFrameFolderName}/output.csv"
df.to_csv(output_path, index=False, encoding="utf-8-sig")
json_data = df.to_json(orient="records")
print('Processing completed!')
