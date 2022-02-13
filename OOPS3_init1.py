#creating multiple instances/Objects using the same class

class Cat:
    def __init__(self,name):
        print(name)

Cat("Goutham")
Cat("Aditi")

#We can store the called class inside a variable for our conveniency

class Cat:
    def __init__(self,name):
        self.name=name #without using the print statemnt, we can simply use this line to store the info inside the class

d=Cat("Prakash")
print(d.name)
r=Cat("Poorani")
print(r.name)

