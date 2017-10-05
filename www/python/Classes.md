# Classes
You can get a long way in Python using the built-in scaler and collection types. For many problems, the built-in types and those available in the Python Standard library are completely sufficient. Sometimes though they aren't quite what's required, and the ability to create custom types is where classes come in.

- Classes define the structure and behavior of objects
- An object’s class controls its initialization.

## Class
- Used to define new classes
- By convention, class names use CamelCase

### Simple class in Shapes module (Shapes.py)
```python
class Rect:
    pass
```
```bash
>>> from shapes import Rect
>>> Rect
<class 'shapes.Rect'>
>>> r=Rect() #create object
>>> r
<shapes.Rect object at 0x02EC0B90>
>>> type(r)
<class 'shapes.Rect'>
```
## Methods
- Method - A function defined within a class
- Instance methods – functions which can be called on objects
- self – the first argument to all instance methods

### Instance methods

Instance methods must accept a reference to the instance on which the method was called as the first argument, and by convention this argument is always called **self**.
```python
class Rect:
    def area(self):
        return 0
```
```bash
>>> from shapes_instance import Rect  
>>> r=Rect()                          
>>> r.area()                          
0                                     
```
## Initializers
the initialization method is called as part of the process of creating a new object when we call the constructor. The initializer method must be called to double underscore init delimited by the double underscores used for Python runtime machinery. Like all other instance methods, the first argument to double underscore init must be self.
- The initializer should not return anything. It simply modifies the object referred to by self.
- We choose **_length** with the leading underscore for two reasons. First, because it avoids a name clash with the method of the same name. Methods are functions, functions are objects, and these functions are bound to attributes of the object, so we already have an attribute called number, and we don't want to replace it. Second, there is a widely followed convention that the implementation details of objects which are not intended for consumption or manipulation by clients of the object should be prefixed with an underscore.
- Constructors are not equivalent to initializers . In python we don't have a constructor

shapes1.py
```python
class Rect:
    def __init__(self, length, breadth):
        self._length = length
        self._breadth = breadth

    def area(self):
        return self._length * self._breadth

r = Rect(10, 20)
print("Area of rectangle: ", r.area())

```
```bash
Area of rectangle:  200
```
## Validating initializer arguments
Validate the arguments passed to initializer and raise an error if they are wrong
shapes2.py
```python
class Rect:
    def __init__(self, length, breadth):
        if length <= 0 or breadth <= 0:
            raise ValueError("Invalid length or breadth")
        self._length = length
        self._breadth = breadth

    def area(self):
        return self._length * self._breadth

r = Rect(10, 20)
print("Area of rectangle: ", r.area())
r = Rect(-10, 20)
print("Area of rectangle: ", r.area())
```
```bash
Traceback (most recent call last):
  File "shapes2.py", line 13, in <module>
Area of rectangle:  200
    r = Rect(-10, 20)
  File "shapes2.py", line 4, in __init__
    raise ValueError("Invalid length or breadth")
ValueError: Invalid length or breadth

```
## Passing Object as argument
Lets Draw object use Rect object and draws rectangle on plane
```python
class Rect:
    def __init__(self, length, breadth):
        if length <= 0 or breadth <= 0:
            raise ValueError("Invalid length or breadth")
        self._length = length
        self._breadth = breadth

    def area(self):
        return self._length * self._breadth

class Draw:
    def write(self, rect):
        print("Drawing rectangle", rect.area())
r = Rect(10, 20)
d = Draw()
d.write(r)
```
```bash
Drawing rectangle 200
```
## Polymorphism
Is condition of occurring in several different forms. There are two types of Polymorphisms compile time and runtime.
Python doesn't have compile time Polymorphism
In below example draw function is able to draw a rectangle or square
shapes4.py
```python
class Rect:
    def __init__(self, length, breadth):
        self._length = length
        self._breadth = breadth

    def area(self):
        return self._length * self._breadth

class Square:
    def __init__(self, side):
        self._side = side


    def area(self):
        return self._side * self._side

def draw(shape):
    print("Drawing shape with area", shape.area())

r = Rect(10, 20)
s = Square(10)

# polymorphic draw function
draw(r)
draw(s)
```
```bash
Drawing shape with area 200
Drawing shape with area 100
```
## Inheritance
Inheritance is way to achieve code reusability. Python supports inheritance, it even supports multiple inheritance. Classes can inherit from other classes. A class can inherit attributes and behaviour methods from another class, called the superclass. A class which inherits from a superclass is called a subclass, also called heir class or child class
employee.py
```python
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_name(self):
        return self._first_name + "," + self._last_name

class Employee(Person):
    def __init__(self, first_name, last_name, emp_id):
        # Call the parent class init
        Person.__init__(self, first_name, last_name)
        self._emp_id = emp_id
    def get_complete_details(self):
        return self.get_name() + "," + self._emp_id

e = Employee("dora", "daneial", "sr4356")
print(e.get_name())
print(e.get_complete_details())
```
```bash
dora,daneial
dora,daneial,sr4356
```
## Overloading
overloadin_demo.py

```python
class Display:
    def show(self, x, y=0, z=0):
        print(x, y, z)

#Create a instance
d = Display()
#Call methods on the instance
d.show(1)
d.show(1, 2)
d.show(1, 2, 3)
```
```bash
1 0 0
1 2 0
1 2 3
```
## Overriding
 Overriding is the ability of a class to change the implementation of a method provided by one of its ancestors
overriding_demo.py
 ```python
 class A:
    def show(self):
        print("I am a")

class B(A):
    # override show behavior
    def show(self):
        print("I am b")

b = B()
b.show()
 ```
 ```bash
 I am b
 ```
overriding_demo_1.py
Call super class method
```python
class A:
    def show(self):
        print("I am a")

class B(A):
    # override show behavior
    def show(self):
        #call the super class method
        A.show(self)
        print("I am b")

b = B()
b.show()
```
```bash
I am a
I am b

```


### [index](index.html)
