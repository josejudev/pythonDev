from http.server import CGIHTTPRequestHandler
from requests.api import delete
from driveFiles.mainDrive import Create_Service
from googleapiclient.http import MediaFileUpload
from getFiles import *
from animate import *
import json, requests
from apiclient import errors


#!crear servicio
CLIENT_SECRET_FILE = "/home/joseju/Documentos/pythonDev/driveFiles/api_drive.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

with open('/home/joseju/Documentos/pythonDev/driveFiles/data_file.json') as f:
    data = json.load(f)

for arch in data["Files"]:
    deleteId = arch["id_file"]

animates()
def delete_file(service, deleteId):
    try:
        service.files().delete(fileId=deleteId, supportsAllDrives=True).execute()
        print("\n ✖ File deleted suscessfully")
        print("\n")
    except errors.HttpError as error:
        print('An error occurred: %s' % error)

delete_file(service, deleteId)        