import os
import shutil
orig = r"C:\Users\donys\Desktop\codes\copy"
dest=r"C:\Users\donys\Downloads\ultra_3.0"
if (os.path.isdir(orig)):
    for fl in os.listdir(orig):
        fileold=os.path.join(orig,fl)
        #print(fileold)
        filenew=os.path.join(dest,fl)
        #print(filenew)
        if(os.path.isfile(filenew)):
          new=os.path.split(filenew)
          print(new)
          newfile=(new[-1])
          print(newfile)
          data=os.path.splitext(newfile)
          onlyname=data[0]
          ext=data[1]
          newbase=onlyname+"_new"+ext
          newname=os.path.join(dest,newbase)
          print(newbase)    
          shutil.copy(fileold,newname)
        else:
            shutil.copy(fileold,filenew)