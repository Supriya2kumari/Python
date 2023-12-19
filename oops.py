# CLASSES AND OBJECTS
class Parrot:
    name = ""
    age = 0
    color = ""
parrot1 = Parrot()
parrot1.name = "nauty"
parrot1.age = 10
parrot1.color = "green"

parrot2 = Parrot()
parrot2.name = "sweety"
parrot2.age = 12
parrot2.color = "light green"

print(f"The age of {parrot1.name} is {parrot1.age} years and color is {parrot1.color}")
print(f"{parrot2.name} is {parrot2.age} years old and the color is {parrot2.color}")


# INHERITANCE
class Animal:
    def eat(self):
        print("I can eat something...")
    def sleep(self):
        print("I can sleep...")
class Dog(Animal):
    def bark(self):
        print("I can bark Bow Bow...")
dog1 = Dog()
dog1.eat()
dog1.sleep()
dog1.bark()


# ENCAPSULATION
class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("selling price : {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computer()
c.__maxprice=1000
c.setMaxPrice(1200)
c.sell()

class LoginCredential:
    def __init__(self):
        self.__username = "Admin"
        self.__password = "Password@123"
    def getDetails(self):
        print("user name : {}".format(self.__username))
        print("password : {}".format(self.__password))
    def setUserDetails(self, username):
        self.__username = username
    def setPassword(self, password):
        self.__password = password

obj = LoginCredential()
obj.getDetails()
obj.setPassword("Strong@password")
obj.getDetails()


# POLYMORPHISM
class Polygon:
    def render(self):
        print("Rendering polygon ")
class Square(Polygon):
    def render(self):
        print("Rendering square")
class Circle(Polygon):
    def render(self):
        print("Rendering circle")
class Triangle(Polygon):
    def render(self):
        print("Rendering triangle")
s = Square()
s.render()
c = Circle()
c.render()
t = Triangle()
t.render()


# MULTIPLE INHERITANCE
class Animal:
    def eat(self):
        print("Eating...")
class Dog:
    def bark(self):
        print("Barking bow bow ...")
class BabyDog(Animal, Dog):
    pass
bdog = BabyDog()
bdog.eat()
bdog.bark()


# MULTILEVEL INHERITANCE
class Animal:
    def eat(self):
        print("Eating....")
class Dog(Animal):
    def bark(self):
        print("Barking....")
class BabyDog(Dog):
    def weep(self):
        print("Weaping....")
bd = BabyDog()
bd.weep()
bd.eat()
bd.bark()


# MRO (METHOD RESOLUTION ORDER)
class Animal:
    def eat(self):
        print("all the animals can eat....")
class Dog:
    def eat(self):
        print("Dog can also eat....")
class BabyDog(Dog, Animal):
    pass
b = BabyDog()
b.eat()


# METHOD OVERRIDING
class Animal:
    name = ""
    def eat(self):
        print("I can eat")
class Dog(Animal):
    def eat(self):
        print("I like to eat bones")
d = Dog()
d.eat()


# USE OF super() METHOD
class Animal:
    name = ""
    def eat(self):
        print("I can eat")
class Dog(Animal):
    def eat(self):
        super().eat()
        print("I like to eat bones")
d = Dog()
d.eat()

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input("Enter side"+str(i+1)+" : ")) for i in range(self.n)]
    def displaySides(self):
        for i in range(self.n):
            print("Side",i+1,"is ",self.sides[i])
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
    def findArea(self):
        a, b, c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**1/2
        print("The area of Triangle is %0.2f" %area)
class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4)
    def findArea(self):
        a, b, c, d = self.sides
        area = a * c
        print("Area of rectangle is %0.5f" %area)
        
t = Triangle()
r = Rectangle()
r.inputSides()
r.displaySides()
r.findArea()
t.inputSides()
t.displaySides()
t.findArea()


#OPERATOR OVERLOADING
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
p1 = Point(5, 6)
p2 = Point(5, 4)
print(p1 + p2)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __lt__(self, other):
        return self.age < other.age
p1 = Person("Radhe", 23)
p2 = Person("Krishna", 21)
print(p1 < p2)