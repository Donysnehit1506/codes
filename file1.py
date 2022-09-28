fh=open("test code.txt","r")
fh1=open("text1.txt","r")

fh2=open("merge.txt","w")
fh2.write(fh.read())
fh2.write(fh1.read())


print("************************")
fh2=open("merge.txt","r")
fh2.seek(70)
print(fh2.read())
    
    
    