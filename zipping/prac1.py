# create a zip file with using python
from zipfile import ZipFile 


f = ZipFile("combine.zip",'w')
f.write("demo1.txt")
f.write("demo2.txt")
f.write("demo3.txt")
f.write("demo4.txt")
f.close()
print("zip file created......")
