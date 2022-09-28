with open("hello.txt","r") as src1, open("hi.txt","r") as src2, open("greet.txt","a") as dest:
    for i in src1.read():
        dest.write(i)
    for i in src2.read():
        dest.write(i)