class Student:
    def __init__(self,rollno=1,name="aleena"):
        self.rollno=rollno
        self.name=name

    def display(self):
        print("rollno={} and name={}".format(self.rollno,self.name))
ob=Student()
ob.display()
ob1=Student(2,"sachin")
ob1.display()
