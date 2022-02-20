class Rate:
    amount=0
    def __iniit__(self,no):
        self.no=no
    
    @classmethod                              #use @classmethod before using this
    def add(cls):                             #first parameter inside a class method must be cls.You can have other parameters as well
        cls.amount+=1                         #We can use class methoddde for operations liike these ass well
        print(cls.amount)                    #use cls and then,the instance which is directly declared  under the class

t=int(input("Enter the no of iterations: "))
for i in range(t):
    Rate.add()