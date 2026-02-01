class student:
    schoolName= "MHS"

    def __init__(self, name , course):
        self.name=name
        self.course=course
        print("init called autumatically when new object  created ")
       
student1= student("saumya","B.E.computer") #init called
print("s1-",student1.name)
print("course",student1.course)

student2= student("parth","B.E.mechanical")
print("s2-",student2.name)
print("course-",student2.course)
# variabeles inside class is attributes 
# function inside class is methods







