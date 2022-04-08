import os, glob, zipfile, time
from datetime import datetime


def new_files():
    #! =>Comprobar si existen archivos
    bakFile = glob.glob("/home/joseju/Documentos/files_backup/*.pdf")
    if bakFile:
        print("\n ✖ Files found")
        
        
    for files in bakFile:
        try:
            print("\t Archivo: → ",files)
        except OSError as e:
            print(f"Error:{ e.strerror}")

    #! =>crear la carpeta con la fecha actual
    if len(bakFile) > 0:
                folderName = datetime.today().strftime('%Y-%m-%d')
                fileDir = f"/home/joseju/Documentos/files_backup/{folderName}"
                if not os.path.exists(fileDir):
                    os.makedirs(fileDir)
    time.sleep(1) 

    #! =>comprimiendo archivos
    zipFolder = zipfile.ZipFile(f'/home/joseju/Documentos/files_backup/{folderName}/{folderName}.zip', 'w')
    path = f'/home/joseju/Documentos/files_backup/{folderName}/{folderName}.zip'

    for folders, subfolders, files in os.walk(f'/home/joseju/Documentos/files_backup/'):
        for file in files:
            if file.endswith('.pdf'):
                zipFolder.write(os.path.join(folders, file), os.path.relpath(os.path.join(folders, file), '/home/joseju/Documentos/files_backup/'))

    zipFolder.close()
    print("\n ✓ Files compressed successfully")
    time.sleep(2)
    return path
    #copiando archivos a la carpeta recien creada
    # source = r'/home/joseju/Documentos/files_backup/'
    # destination = r'/home/joseju/Documentos/files_backup/'+folderName

    # files = glob.iglob(os.path.join(source, '*.bak'))

    # for file in files:
    #     if os.path.isfile(file):
    #         shutil.copy2(file, destination)