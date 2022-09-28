'''num1 = 25_000_000
num2 = 25000000
print(num1,num2)'''

'''num = 1.75e5
print(num)'''

#print(2e308)

'''base = input("enter a base : ")
exponent = input("enter an exponent")
res = float(base) ** float(exponent)
print(f"{base} to the power of {exponent} = {res}")'''

'''user = input("enter a number : ")
num = float(user)
print(f"{num} rounded to 2 decimal places is {round(num,2)}")'''

'''num1 = float(input("enter a number : "))
num2 = float(input("enter a number : "))
print(
    f"the differecne between {num1} and {num2} is an integer?"
    f"{(num1-num2).is_integer()}"
)'''

'''print(f"{3 ** .125:.3f}")
print(f"${150000:,.2f}")
print(f"{2/10:.0%}")'''

'''def cube(num):
    cubenum = num**3
    return cubenum
print(f"0 cubed is {cube(0)}")
print(f"2 cubed is {cube(2)}")'''

'''def greet(name):
    """Display a greeting."""
    print(f"hello {name}!")
greet("dony")'''

'''def convertCF(tempcel):
    """return the celsius temprature tempcell converted to fahrenheit"""
    tempfar = tempcel * (9/5) + 32
    return tempfar   
def convertFC(tempfar):
    """return the fahenheit temperature tempfar convert to celsius"""
    tempcel = (tempfar - 32) * (5/9)
    return tempcel
tempfar = input("enter the temprature in F : ")
tempcel = convertFC(float(tempfar))
print(f"{tempfar} degree F = {tempcel:.2f} degree C")
print(f"{tempfar} degree F = {round(tempcel,2)} degree C")
tempcel = input("\nenter the temperature in degrees of C : ")
tempfar = convertCF(float(tempcel))
print(f"{tempcel} degrees C = {tempfar:.2f} degrees F")'''

'''def doubles(num):
    """return the result of multiplying an input number by 2."""
    return num * 2
mynum = 2
for i in range(0,3):
    mynum = doubles(mynum)
    print(mynum)'''

'''def invest(a,r,y):
    for y in range(1,y+1):
        a=a*(1+r)
        print(f"year {y} :${a:,.2f}")
a = float(input("enter the amount : "))
r = float(input("enter the rate of returnt : "))
y = int(input("enter the number of years : "))
invest(a,r,y)'''

t = ()
num1 = int(input("how many numbers")) 
for i in range(num1):
    num2 = int(input("emter the numbers"))
    t.add(num2)
    print(t)
    print(hash(t))