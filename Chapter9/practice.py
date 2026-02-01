class student:
    def __init__(self, name ,marklist):
        self.name=name
        self.marklist=marklist

    def average(self):
        sum=0
        for each in self.marklist:
            sum=sum+each
        average=sum/3
        print("average is-",average)

stu1= student("parth",[90,98,99])
stu1.average()

