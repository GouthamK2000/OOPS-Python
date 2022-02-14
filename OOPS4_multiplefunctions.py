#Use multiple functions inside a class

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getname(self):
        return self.name 

    def getage(self):
        print(self.age)
    
#Above functions must ahve self. used, ebven if print statemnet is used instead of return

d=Dog("Goutham","21")
print(d.name)
d.getage()

#Above we ghave seen how to  print 2 different ways to print the output.....
#We can use the age,name, inside __init__ function.But , we have to use self.name and self.age inside other functions inside the class, below, the __init__ function.