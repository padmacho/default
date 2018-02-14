# Interview Questions
This page covers Interview Questions that you might come across in python developer role

# What are the key features of Python?
- Interpreted Language
    - Unlike languages like C or C++ and its variants, Python does not need to be compiled before it is run.
- Dynamically typed
    - You don’t need to say the type of variable when you declare them.
    ```Python
    a = 123
    a = 'I am a string'
    a = 12.3
    ```
- Object orientated
    - It allows the definition of classes along with composition and inheritance. It doesn't have access specifiers like public, private.
- Functions
    - Functions are first-class objects. This means that they can be assigned to variables, returned from other functions and passed into functions. **Classes** are also first class objects.
    ```Python
    # Assign function a variable
    def fun1():
        print("Hello")
x = fun1
x()  # Call x as function
fun1()
    ```

    ```python
    # Function return a return a function
def fun1():
    print("Hello fun1")
def fun2():
    return fun1
fun2()() # call the returned function
    ```
    ```python
    # Function be passed as argument
def fun1():
    print("Hello fun1")
def fun2(f):
    f()
fun2(fun1)  # Pass fun1 as argument to fun2
    ```



# What is difference  between deep copy and shallow copy ?
- Assignment statements in Python do not copy objects

```Python
# List Bag1 one has fruits
bag1 = ['apple', 'banana']

# Lets create a Bag2 which has the same fruits as Bag1
bag2 = bag1  # Assignment statements in Python do not create a copy of object

print('Bag1: ', bag1)
print('Bag2: ', bag2)

# remove apple from bag1 which will effect bag2 as well
del bag1[0]

# Notice apple is removed from both the bags instead from bag1
print('Bag1: ', bag1)
print('Bag2: ', bag2)

```
```bash
Bag1:  ['apple', 'banana']
Bag2:  ['apple', 'banana']
Bag1:  ['banana']
Bag2:  ['banana']
```
- Python defines a module which allows to deep copy or shallow copy mutable object using the inbuilt functions present in the module **copy**

#
