a = 123
a = 'I am a string'
a = 12.3


# Assign function a variable
def fun1():
    print("Hello")


x = fun1
x()  # Call x as function
fun1()


# Function return a return a function

def fun1():
    print("Hello fun1")


def fun2():
    return fun1


fun2()()  # call the returned function


# Function be passed as argument

def fun1():
    print("Hello fun1")


def fun2(f):
    f()


fun2(fun1)  # Pass fun1 as argument to fun2
