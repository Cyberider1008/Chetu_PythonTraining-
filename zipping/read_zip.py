#read a zip file

from zipfile import ZipFile

f = ZipFile("combine.zip","r")
l = f.namelist()
for name in l:
    print(name)
