#file = r"C:\Users\donys\Desktop\codes"
#if (os.path.isfile(file)):
#    print("it's a file")
#elif(os.path.isdir(file)):
#        print("it's a folder")
#else:
#    print("it's not a file or folder")'''

import os
import shutil
old = r"C:\Users\donys\Desktop\codes\fh.py"
new = r"C:\Users\donys\Desktop\codes\copy\fh.py"
shutil.copy(old,new)