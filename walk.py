import os
import shutil
li=[]
pat=".py"
for dir,sdir,fn in os.walk(r""):
    for i in list(fn):
        li.append(os.path.splitext(i)[1])
        print(li)
        for i in li:
            if i == pat:
                shutil.copyfile(i,r"")