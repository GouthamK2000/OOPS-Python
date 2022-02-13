class Dog:
    def __init__(self,name):
        print(name)

Dog("Goutham")
#automatically, this name is assigned to the value, next to the self parameter.

# multiple parameters inside a class, inside __init__
class Cat:
    def __init__(self,name,age):
        print("I am "+name+" i am "+age+ " years old!")

Cat("Goutham","21")
