from random import randint
tosses=[]
head=tail=0
for i in range(0,2):
    while(randint(0,1)==0):
        tail+=19
        tosses.append("T")
    head+=1
    tosses.append("H")
print(head,tail)
print(head/tail)
print(tosses)