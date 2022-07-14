from curses.ascii import NAK
from errno import ELIBBAD
from pip import main
from driveFiles.mainDrive import Create_Service
from googleapiclient.http import MediaFileUpload
from getFiles import *
from animate import *
import json, time
from shutil import rmtree


def cloudDrive():
    CLIENT_SECRET_FILE = "/home/joseju/Documentos/pythonDev/driveFiles/api_drive.json"
    API_NAME = "drive"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/drive"]

    bakFile = os.listdir("/home/joseju/Documentos/files_backup")
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    zipName = bakFile[0]
    animates()

    #! =>Crear folder en drive
    try :
        folder = service.files().create(body={'name': zipName, 'mimeType': 'application/vnd.google-apps.folder'},
                                        fields='id').execute()
        print("\n ✓ Folder created successfully Cloud")
        time.sleep(2)
    except Exception as e:
        print(f"Error:{ e.strerror}")

    #! =>Subir archivo comprimido a Google Drive
    FOLDER_ID = folder.get('id')
    FILE_NAMES = [zipName]
    MIME_TYPES = ["application/zip"]
    try:
        for file_name, mime_type in zip(FILE_NAMES, MIME_TYPES):
            file_metadata = {
                "name": file_name,
                "parents": [FOLDER_ID]
            }

            media = MediaFileUpload(new_files(),mimetype=mime_type)
            service.files().create(
                body=file_metadata, media_body=media, fields="id"
                ).execute()

        print("\n ✓ ☁ File uploaded successfully")
        time.sleep(2)
    except Exception as e:
        print(f"Error:{ e.strerror}")
    deleteFolder()

def deleteFolder():
    bakFile = os.listdir("/home/joseju/Documentos/files_backup")
    x = 0
    while True:
        try:
            rmtree(f'/home/joseju/Documentos/files_backup/{bakFile[x]}')
            x = x+1
            if bakFile:
                cloudDrive()
            else:    
                if x == len(bakFile):
                    break
        except Exception as e:
            print(f"No files found")
            break

cloudDrive()



# Utilidades!

#! =>Guardar datos en json file
# data = {}
# data['Files'] = []
# try :
#     data['Files'].append({
#             'id_file': folder.get('id'),
#             'data_create': zipName})

#     with open('/home/joseju/Documentos/pythonDev/driveFiles/data_file.json', 'w') as file:
#             json.dump(data, file, indent=4)
#     print("\n ✓ Json file created successfully")
#     time.sleep(2)
# except Exception as e:
#     print(f"Error:{ e.strerror}")



#!listar archivos de drive
# folder_id = "1IN7t24bzlloAJqlfpq-JTteX2E0BJjUp"

# query = f"parents: '{folder_id}'"

# response = service.files().list(q=query).execute()
# files = response.get('files')
# nextPageToken = response.get('nextPageToken')

# while nextPageToken:
#     response = service.files().list(q=query).execute()
#     files.extend(response.get('files'))
#     nextPageToken = response.get('nextPageToken')

# df = pd.DataFrame(files)
# print(df)
#?----------------------------------------------------------------------------------------------------------------------