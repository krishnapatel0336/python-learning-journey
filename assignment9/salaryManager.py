# practice4

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percentage):
        increment = self.salary * (percentage / 100)
        self.salary += increment


employee1= Employee("SaumyaSingh", 1000000)
employee1.increase_salary(50)
print("Name Of Employee:",employee1.name)
print("SalaryAfterRise:",employee1.salary )







