import os
'''fh=open("C:/Users/donys/Documents/Arduino/calibrater/Arduino3.txt","a")
fh.write("As its written in Java language")
fh.close()


fr=open("C:/Users/donys/Documents/Arduino/calibrater/Arduino3.txt","r")
print(fr.read(10))
fr.close()

os.rename("C:/Users/donys/Documents/Arduino/calibrater/Arduino3.txt","C:/Users/donys/Documents/Arduino/calibrater/Javalangs.txt")
#os.rename("result.py.html","answer.py")
os.remove("C:/Users/donys/Documents/Arduino/calibrater/Arduino.txt")
os.mkdir("C:/Users/donys/Documents/Arduino/calibrater/python-prctise")
os.rmdir("C:/Users/donys/Documents/Arduino/calibrater/python-prctise")'''
os.chdir("C:/Users/donys/Desktop/codes/")
file=open("test code.txt","w")
file.write("hello world!")
file.close()
print(os.getcwd())