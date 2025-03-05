# Define a python class Person with instance object variables name and age.
# Set Instance object variables in init () method. Also define show() method to display name and age of a person.
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age    
    def show(self):
        print("Name is :",self.name)
        print("Age is :",self.age)

obj=Person("Sanket", 23)
obj.show()



# Define a class Circle with instance object variable radius.
# Provide setter and getter for radius. Also define getArea() and getCircumference() methods.

class circle:
    def __init__(self, radius=None):
        self.radius=radius   
    def setradius(self,radius):
        self.radius=radius
    def getradius(self):
        return self.radius
    def getarea(self):
        return 3.14*self.radius * self.radius        
    def getcircumference(self):
        return 2*3.14*self.radius
aa=circle(4)
print("Radius is :", aa.getradius())
print("Area is :", aa.getarea())
print("Circumference is :", round(aa.getcircumference(),2))



# Define a class Rectangle with length and breadth as instance object variables.
# Provide setDimensions(), showDimensions() and getArea() method in it.

class Rectangle:
    def setdimensions(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def showdimensions(self):
        print("Length is:", self.length ," and Breadth is:", self.breadth)   
    def getarea(self):
        return self.length * self.breadth
bb = Rectangle()
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
bb.setdimensions(length,breadth)
bb.showdimensions()
print("Area is:",bb.getarea())



# Define a class Book with instance object variables bookid, title and price.
# Initialise them via init () method. Also define method to show book variables.

class book:
    def __init__(self, bookid, title, price):
        self.bookid=bookid
        self.title=title
        self.price=price
    def show(self):
        print("Book Id :", self.bookid, "Title :" ,self.title, "Price :", self.price)
bookid = int(input("Enter book id :"))
title = input ("Enter the title :")
price = float(input("Enter the price :"))
bk=book(bookid,title,price)
bk.show()



# Define a class Team with instance object variable a list of team member names.
# Provide methods to input member names and display member names.

class team:
    def __init__(self):
         self.lst=[]
    def inplst(self):
        num_members=int(input("Enter number of members :"))
        for i in range(num_members+1):
            name=input("Enter name of team member:")
            self.lst.append(name)
            i+=1      
    def display(self):
        print(self.lst)
dd=team()
dd.inplst()
dd.display()
