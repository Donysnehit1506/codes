intial=int(input("enter the intial number : "))
final=int(input("enter the final number : "))
print("\nEVEN AND ODD NUMBERS")
es=os=0
print("------------------")
print("EVEN NUMBERS")
print("*************")
for i in range(intial,final+1):
    if(i%2==0):
        es=es+i
        print(" ")
        print("===>",i)
        print("factors of",i,"are : ")
        for j in range(1,i+1):
            if i % j == 0:
                print(j)
print("--------------------------")
print("ODD NUMBERS")
print("*************")
for i in range(intial,final+1):
    if(i%2!=0):
        os=os+i
        print(" ")
        print("===>",i)
        print("factors of",i,"are : ")
        for j in range(1,i+1):
            if i % j == 0:
                print(j)
print("-----------------------------------")
print("sum of even numbers are : ",es)
print("sum of odd numbers are : ",os)