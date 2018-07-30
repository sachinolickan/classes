class List:
    def __init__(self,size):
        self.list=list()
        self.size=size
        
    def append(self):
        l1=self.list
        for i in range(self.size):
            l1.append(int(input()))
        

    def remove(self):
        l1=self.list
        x=int(input("enter a number to remove:"))
        for j in l1:
            if(x==j):
                l1.remove(j)
            
    def display(self):
        l1=self.list
        print(l1)
        
y=int(input("size of the list"))


ob=List(y)
ob.append()
ob.remove()
ob.display()
                
            
        
