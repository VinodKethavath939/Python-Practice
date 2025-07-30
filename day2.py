def my_function(*kids):
    print("The youngest child is "+ kids[2])
my_function("Email","Tobias","Linus") 

def my_funnction(**kid):
    print("He is my youngest son " + kid["super"])
my_funnction(fname="Hero",super="superman")  

def my_function(food):
    for x in food:
        print(x)

fruits=["apple","banana","Mango"]
my_function(fruits)

x=lambda a:a+10
print(x(5))

def myfunc(n):
    return lambda a :a*n
mydoubler =myfunc(2)
print(mydoubler(11))

x=lambda a:a+10
print(x(5))  

x=lambda a:a*2
print(x(5))

pairs = [(1, 2), (3, 1), (5, 0)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age= age
p1 = Person("John",36)
print(p1.name)
print(p1.age)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def __str__(self):
        return f"{self.name}({self.age})"
p1 = Person("John",36)
print(p1)

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks 
    def display(self):
        print(f"Name:{self.name},Marks:{self.marks}")
s1 = Student("Alice",86)
s1.display()

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(f"brand:{self.brand},model:{self.model}")
c1=Car("Thar",2025)
c1.display()
        