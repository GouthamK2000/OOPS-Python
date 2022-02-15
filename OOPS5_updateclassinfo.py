class  students:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getage(self):
        return self.age

    def updateage(self,age):
        self.age=age
        return age

stud=students("Gotuham",21)
print(stud.getage()) #printing the initial age
print(stud.updateage(25)) # value of the age got updated here