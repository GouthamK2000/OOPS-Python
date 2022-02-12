#returns the type  we use

def hello():
    print("hello")

print(type(hello())) #returns <class 'Nonetype'>
print(type(hello)) #returns <class 'function'>

r=9
print(type(r)) #returns <class 'int'>

t="goutham"
print(type(t)) #  returns <class 'str'>


t="temper"
print(t.upper()) #returns the upper value. the 'method'(.upper()) is acting on the 'object' (t), which is a string.This method can work only on strings
 