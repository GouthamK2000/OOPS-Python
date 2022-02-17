""" 

class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self):
        print("Meow")

class Dog:
    def __init(self,name,age):
        self.name=name
        self.age=age
    
    def speak(self):
        print("Bark")

There are many things repeated in both the classes.Declaring all the components  that are common in both the classes under one class and then
inheriting the common properties into other clases is actually inheritance.WE do the following for that. """

class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I am speechless")

class Dog(Pet):
    def speak(self):
        print("barks")

class Cat(Pet):
    def speak(self):
        print("Meow")

class Fish(Pet):
    pass

# assign the common class to a variable initially.
p=Pet("Goutham",21)
p.show()#We call the inital common class and it works perfect.
d=Dog("Boomer",20)
d.show()#We call the Dog class and it works perfect.
c=Cat("Tom",19)
c.show()#We call the Cat class and it works perfect.

f=Fish("Bubbles",18)
f.show()

p.speak() # speak func inside Cat class works perfectly
d.speak() # speak func inside Dog class works perfectly
c.speak() # speak function inside the common class works perfectly
f.speak()

#If 2 functions are defined inside the same class, with same name, then the one defined last will be executed.....
#If suppose a third pet was declared and we use "pass", what comes in the output when we call for speak() function is the content under the speak
#function in common class


