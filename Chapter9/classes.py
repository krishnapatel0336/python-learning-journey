# class creation
class vehical:
    #attributes
    color="black" 
    fuel="petrol"
    mileage="10"

# Object creation
car= vehical()
print(car.color)
bike= vehical()
fighterJet= vehical()
# above 3 are objects of vehical class :

# practice 1 

class car:
    brand= "Scorpio"

obj1= car()
print("brandName is-", obj1.brand)

# practice 2 
# laptop class with  some attributes
class laptop:
    brand= "default"
    RAM= "default 8GB"
    price= "default 1 lakh"

obja= laptop()
obja.brand= "Mackbook"
obja.RAM="16GB"
print("laptop1-Brand-", obja.brand)

objb= laptop()
objb.brand= "VIVObook"
print("laptop2-Brand-", objb.brand)
