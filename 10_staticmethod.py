class Math:

    @staticmethod     #static method does not involve any changes. Info under this is static.

    def add5(x):
        return x+5

    def add4(y):      # NO need of the self parameter for the functions, which are under @staticmethod.
        return y+7

    def pri():
        print("Print")

print(Math.add5(10))
print(Math.add4(10))
Math.pri()

#Self parameter is not required for @static method because, we are not accessing anything from the class.
