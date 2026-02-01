# practice2: Cretor portfolio
    
class Creator:
       def __init__(self, name , username):
          self.name = name
          self.username = username

       def bio(self):
        return f"Name: {self.name}, Username: @{self.username}"
# object
person1= Creator("Rahul Paramar", "Rahul123")
person1.bio()
print(person1.bio())


