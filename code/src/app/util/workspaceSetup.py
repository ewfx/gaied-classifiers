
import shutil
import os

def setupWorkspace(PropcessingFolderPath,dataFrameFolderName):
    shutil.rmtree(PropcessingFolderPath, ignore_errors=True)
    os.makedirs(PropcessingFolderPath, exist_ok=True)
    shutil.rmtree(dataFrameFolderName, ignore_errors=True)
    os.makedirs(dataFrameFolderName, exist_ok=True)