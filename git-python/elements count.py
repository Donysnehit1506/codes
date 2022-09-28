file=r"C:\Users\donys\Desktop\codes\Clang.txt"
fh = open(file,"r")
upper=lower=num=others=0
read=fh.read()
for i in range (len(read)):
    if read[i].isupper():
        upper+=1
    elif read[i].islower():
        lower+=1
    elif read[i].isnumeric():
        num+=1
    else:
        others+=1
print(upper,lower,num,others)