class Calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        self.add=self.num1+self.num2
        print("result=",self.add)
    def sub(self):
        self.sub=self.num1-self.num2
        print("result=",self.sub)
    def mul(self):
        self.mul=self.num1*self.num2
        print("result=",self.mul)
    def div(self):
        self.div=self.num1/self.num2
        print("result=",self.div)

              
print("enter two numbers")
a=int(input("number:"))
b=int(input("number:"))



ob=Calculator(a,b)

print("choose an operator +,-,/,*:")
st=input()
if(st=='+'):
    ob.add()
elif(st=='-'):
    ob.sub()
elif(st=='/'):
    ob.div()
elif(st=='*'):
    ob.mul()
else:
    print("oprator not found")

        
