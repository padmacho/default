# help
The **help()** method calls the built-in Python help system.
General Syntax:
```python
help(object)
```

# help related to a function
To get help relate to **sqrt** function in **math** module.
- Import the math Module
- Pass sqrt function as argument to help function

```python
>>> import math
>>> help(math.sqrt)
Help on built-in function sqrt in module math:

sqrt(...)
    sqrt(x)

    Return the square root of x.
```
# help relate to a module
Get help related to **math** module

```python
>>> import math                                                 
>>> help(math)                                                  
Help on built-in module math:                                   

NAME                                                            
    math                                                        

DESCRIPTION                                                     
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.           

FUNCTIONS                                                       
    acos(...)                                                   
        acos(x)                                                 

        Return the arc cosine (measured in radians) of x.       

    acosh(...)                                                  
```
Note: Press **q** to quit the prompt
# interactive use.
The help() method is used for interactive use.
```python
>>> help()

Welcome to Python 3.6's help utility!
help> print                                                                             
Help on built-in function print in module builtins:                                     

print(...)                                                                              
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)                  
```
# [Python Home](index.html)
