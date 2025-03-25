# app/global_vars.py

# Folder and file paths
ProcessingFolderPath = "app/Processing"
dataFrameFolderName = "app/DataFrames"
EmailsFolderPath = "app/Emails"

# CSV dataset names
emailHeaderDataSet = "emails_header.csv"
emailAttachmentDataSet = "emails_attachment.csv"

# Email templates
EmailHeaderTemplate = ["Id", "Sender", "Body", "Subject", "Attachments","EmailFileName"]
EmailAttachmentTemplate = ["MailId", "AttachmentID", "FileName", "Text"]

# File extension
MsgExtension = ".msg"
