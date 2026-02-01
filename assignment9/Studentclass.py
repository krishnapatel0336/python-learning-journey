# practice1: student class and get percentage

class student:
    # cast="OBC"//attributes
    def __init__( self , name , Class , marks):
      # init constructor (func)
      self.name= name
      self.Class= Class
      self.marks = marks
      
    def get_percentage(self):
       if self.marks >=0:
        return (self.marks/50)*100
       else:
        return 0
    
 # object
student1= student("raj","CE1", 47)
print(student1.marks , student1.name , student1.Class)
student1.get_percentage()

print(student1.get_percentage(),"%")




    

    

    



     
      
       
