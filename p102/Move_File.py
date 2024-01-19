import os
import shutil

from_dir = "C:/Users/Kalyan/Downloads"
to_dir = "C:/Users/Kalyan/Documents/Document_Files"

list_of_files = os.listdir(from_dir)

for file in list_of_files:
    name,ext=os.path.splitext(file)
    if ext=='':
        continue
    if ext in ['.txt','.doc','.docx','.pdf']:
        path1=from_dir + '/' + file
        path2=to_dir + '/' + "Document_Files"
        path3=to_dir + '/' + "Document_Files" + '/' + file
        if (os.path.exists(path2)):
            print("moving " + file + '...')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving " + file + '...')
            shutil.move(path1,path3) 
