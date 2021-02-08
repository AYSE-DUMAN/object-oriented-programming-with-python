class Parrot:
    
    # class attribute
    species = "bird"

    # instance attribute
    # It is the initializer method that is first run as soon as the object is created.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))

# call our instance methods
print(blu.sing("la la la la la la"))
print(blu.dance())


class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print("Hello")

harry = Person()
print(Person.greet)
print("------------------")
print(harry.greet)
print("****************")
print(harry.greet())
print("..................")


class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i
    def get_data(self):
        print(f'{self.real} + {self.imag}j')

num1 = ComplexNumber(2,3)
num1.get_data()

num2 = ComplexNumber()
num2.get_data()

num3 = ComplexNumber(5)
num3.attr = 10
print(num3.real,num3.imag,num3.attr)

del num1.imag
num1.get_data()

del ComplexNumber.get_data
num2.get_data()



######################## INHERITANCE ########################

# Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed
# class is a derived class (or child class).Similarly, the existing class is a base class (or parent class).

# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")
    
    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function 
        super().__init__() #  we use the super() function inside the __init__() method. This allows us to
        print("Penguin is ready!") # run the __init__() method of the parent class inside the child class.

    def whoisThis(self):
        print("Penguin")
    
    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


#child class without initializing parent __init__ method
class Penguin(Bird):
    
    def __init__(self):
        print("Penguin is ready!")
   
    def whoisThis(self):
        print("Penguin")
    
    def run(self):
        print("Run faster")

peggy2 = Penguin()
peggy2.whoisThis()
peggy2.swim()
peggy2.run()


################################## Encapsulation #########################

# Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct
# modification which is called encapsulation. In Python, we denote private attributes using underscore
#  as the prefix  i.e single _ or double __.

class Computer:

    def __init__(self):
        self.__maxprice = 900 # private attributes

    def sell(self):
        print("Selling Price : {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price 

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()



####################################### Polymorphism ########################

# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
# Suppose, we need to color a shape, there are multiple shape options (rectangle,square, circle).
# However we could use the same method to color any shape. This concept is called Polymorphism.


class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface

def flying_test(bird):
    bird.fly()

# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)



# Python Multiple Inheritance

class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

print(issubclass(list,object))
print(MultiDerived.__mro__)


my_list = [1,2,3]

my_iter = iter(my_list)

print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


