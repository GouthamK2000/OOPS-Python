class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"I am {self.name} and I am {self.age}years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    def __init__(self,name,age,color): #arguments inside the parent classes are called again, but no need to  do self.argument=argument again.
        super().__init__(name,age) #super function refers to the parent class.Arguments inside it should be the parameters that are definied in super class,without self.
        self.color=color
    
    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old! I am {self.color} in color")


p=Pet(" GOutham "," 21 ")
p.speak()
p.show()
c=Cat("Boomer","12","BLack")
c.show()
c.speak()

#This method is used when there is one or more arguemnts in the __init__ function of the child class. There can be any no, of arguments, but we use this for
#additional  arguemnts