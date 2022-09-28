fh=open("file2.txt","w")
fh.write("hello world ")
fh.write(" this is dony")
fh.close()

with open("file2.txt", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print (word)
