# Primitive Scalar Types
Python comes with a number of built-in data types. These include primitive scalar types, like **int**,**float**,**bool** and **None** as well as collection types, like **dictionaries**.

# int
Integer literals in python can be specified in decimal, binary, octal and hexadecimal
```python
# decimal
>>> 10                      
10       
# binary                   
>>> 0b10                    
2                           
# octal
>>> 0o10                    
8      
# hexadecimal                     
>>> 0x10                    
16                          
```
## Convert other types to integer
**int** constructor can be used to convert other data types like string, float to int
```python
# Convert float to integer
>>> int(2.5)
2
# Convert String to integer
>>> int("143")
143
```
# float
Python floats are implemented as IEE-754 double precision floating-point numbers with 53 bits of binary precision. This is equivalent to between 15 and 16 significant digits in decimal.
```python
>>> pi=3.1415926535            
>>> pi                         
3.1415926535
# Scientific notation can also be used for large numbers
>>> speed_of_light=3e8         
>>> speed_of_light             
300000000.0                    
# Smaller numbers
>>> planck_constant=6.62e-34   
>>> planck_constant            
6.62e-34                       
>>> type(planck_constant)      
<class 'float'>                
```
## Convert other types to float
**float** constructor can be used to convert other data types like string, integer to float
```python
>>> float(4)
4.0
>>> float("4.5")
4.5
# construct not a number
>>> float("nan")
nan
# positive infinity
>>> float("inf")
inf
# Negative infinity
>>> float("-inf")
-inf
# int and float operation is promoted to float
>>> 4.3+1
5.3
```
# NoneType
Python has a special null value called None it represent the absence of a value
```python
# None value is not printed to REPL
>>> None
>>> x=None
>>> x is None
True
```
# bool
The bool type represents logical states .There are two bool values, True and False, both with initial capitals.
```python
>>> True        
True            
>>> False       
False           
>>> x = True    
>>> x           
True            
>>>     
```
## Convert other types to bool
bool constructor can be used to convert other types to boolean
 - 0 is considered as False rest all are True
 - empty collection is False rest all are True
 - empty string is false rest all are True
```python
>>> bool(0)           
False                 
>>> bool(0.0)         
False                 
>>> bool(1)           
True                  
>>> bool(1.2)         
True                  
# Empty lists are always false
>>> bool([])          
False                 
>>> bool([1,2])       
True                  
# Empty string is false
>>> bool("")          
False                 
# Note below is not empty string
>>> bool(" ")         
True                  
# Note false is not empty string
>>> bool("False")     
True                  
```

# Bytes used by data types
Memory size of Python primitive data types depends largely on the Operating System architecture. Below size computed on my Windows 10 OS

Data Type| Bytes| Examples| Remarks
--- | --- | --- | ---
int| 14 bytes| 102|arbitrary precision integer
float|16 bytes| 4.2| 64-bit !oating point numbers
NoneType|8 bytes| None| the null object
bool| 14 bytes | Ture or False| boolean logical values
```python
>>> import sys
>>> sys.getsizeof(2)
14
>>> sys.getsizeof(2.0)
16
>>> sys.getsizeof(True)
14
>>> sys.getsizeof(None)
8
```
# [Python Home](index.html)
