import os
import shutil

fromdir = "/Users/gurje/Downloads/"
todir = "/Users/gurje/Downloads/"

listOfFiles = os.listdir(fromdir)
#print(listOfFiles)
for filename in listOfFiles:
    name, extention = os.path.splitext(filename)
    if extention == "":
        continue
    if extention in ['.txt','.doc', '.docx', '.pdf']:
        path1 = fromdir + '/' + filename
        path2 = todir + '/' + "documentfiles"
        path3 = todir + '/' + "documentfiles" + '/' + filename
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1, path2)
        else:
            os.mkdir(path2)
            print("moving to other")
            shutil.move(path1, path3)
