'''fh = open("text1.txt","w")
fh.write("Hello\nI am Dony\nI am into coding\nI finished my 2nd year")
fh.close()'''

fh1 = open("text1.txt","r")
u=l=n=o=0
for i in fh1.read():
    if i.isupper():
        u=u+1
    elif i.islower():
        l+=1
    elif i.isnumeric():
        n=n+1
    else:
        o=o+1
print(u,l,n,o)
fh1.close()