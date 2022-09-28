import os
src=os.getcwd()
print(src)
print(os.listdir())
os.chdir("C:/Users/donys/Desktop/codes/copy")
print(os.getcwd())
os.system('copy src+"\/main.py" dst+"\/main.py"')