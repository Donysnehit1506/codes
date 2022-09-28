file=(open(r"C:\Users\donys\Desktop\codes\file2.txt","r"))
read=file.read()
print(read)
words=read.split()
words.reverse()
print(words)
print(" ".join(words))

'''for i in reversed(read):
    print(i,end="")'''
