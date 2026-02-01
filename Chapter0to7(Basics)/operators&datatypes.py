#arithmetic
x=18
y=15
print(x+y , x-y , x*y , x^y , x/y, x%y  )
z=x+y
print("value of sum is", z)

#comparison
print(x>y , x<y , x==y , x!=y  )

#logical
print(x>y or x<y, x>y and x<y  , not (x==y))

# print sum and diff:

#input two numbers and print their sum
input3= int(input("enter first number"))
input2= int(input("enter second number"))
sum= input2 + input3
print("sum of the 2 value is", sum)



# diff
a=int(input("first value"))
b=int(input("second value"))
diffrence= a-b
print("solution:", diffrence)

# implcit and explisit function:

#implicit 
x=20 #int
y=("type here") #str
z=5.5 #float

#explicit 
#que 1
#take number input convert it into float
#eg1
y=int(x)
z=float(y)
print("coversion:", z)
print(type (z))
#eg2

num=int(input("enter a value:"))
convertedvalue = float(num)
print("original value is", num, "datatype:", type(num))
print ("convertable value is", convertedvalue, "datatype :", type(convertedvalue))

# Data types
food="pizza"
age=24
area=9.5
name="rolls-royes"
print (type (name)),"/n"
print(type(age))
print(type(area))
#exercise
age2= input ("enter your age :" )

print("data type is :", type( age2 ))
print("value entered is :", age2 )
#keywords cannot be used as variable


