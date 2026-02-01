# practice3

class FoodOrder:
     def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

     def calculate_bill(self):
        return self.quantity * self.price
     

# object
item1= FoodOrder("IceCream",3,50)
item1.calculate_bill()
print(item1.name,"," , item1.quantity ,",",item1.price,"INR")
print("bill:",item1.calculate_bill())