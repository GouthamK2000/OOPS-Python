# class Person: 
#      no_of_people=0               # this section is involved only if they want something is constant for all attributes/objects
#      def __init__(self,name):
#          self.name=name
         

# p1=Person("Goutham")
# print(p1.name)      Here you can also use use Person.name here
# print(p1.no_of_people)

#to increment people gradually

class Person:
    no_of_people=0
    def __init__(self, name):
        self.name=name  
        Person.no_of_people+=1  #include the class name .value, to perform operations on the number

p1=Person("Goutham")
print(f"No of people,{p1.name}="+str(Person.no_of_people))
p2=Person("Prakash")
print(f"No of people,{p2.name}="+str(Person.no_of_people))

