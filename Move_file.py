import os
import shutil

from_dir = "C:/Users/Divyashek/Downloads"
to_dir = "C:/Users/Divyashek/Desktop/Document_files"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:

    name,extension = os.path.splitext(file_name)

    if extension == "":
        continue
    if extension in  [".txt",".doc",".docx",".pdf"]:
        path1 = from_dir+"/"+file_name
        path2 = to_dir+"/"+"Document_files"
        path3 = to_dir+"/"+"Document_files"+"/"+file_name

        #print("path1",path1)
        #print("path3",path3)

        if os.path.exists(path2):
            print("Moving "+ file_name + "....")

            shutil.move(path1,path3)

        else : 
            os.makedirs(path2)
            print("Moving "+ file_name + "....")

            shutil.move(path1,path3)    