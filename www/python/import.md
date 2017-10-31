# import
import functions, classes , objects ,variables from a module. Lets try to import few mathematical functions for math module

General import Syntax
```bash
import module1, module2,... moduleN
```
# Import all functions from math module
Lets import **all** function from **math** module
```python
>>> import math
>>> math.pow(2,3)
8.0
>>> math.exp(1)
2.718281828459045
```
```python
>>> from math import *  
>>> pow(2,3)            
8.0                     
>>> exp(1)              
2.718281828459045       
>>> ceil(2.6)           
3                       
>>>                     

```
# Import specific function from module
Lets try to import only **pow** function from **math** module
```python
>>> from math import pow               
>>> pow(2,3)                           
8.0                                    
>>> exp(1)                             
Traceback (most recent call last):     
  File "<stdin>", line 1, in <module>  
NameError: name 'exp' is not defined   
>>>                                    
```
In the above example **exp** is not imported thats the reason we received an error

# Import more than one function from a module
Lets try to import **pow,exp** from **math** module
```python
>>> from math import pow,exp
>>> pow(2,3)
8.0
>>> exp(1)
2.718281828459045
>>> ceil(2.3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ceil' is not defined
```
Note: Though we have **ceil** function in math module but we are unable to use it because we didn't import it
# Import more than one module
Lets import **math** and **sys** Modules
```python
>>> import math,sys   
>>> math.pow(2,3)     
8.0                   
>>> sys.argv          
['']                  
>>>                   

```
Note: **argv** is attribute from sys module

# [Python Home](index.html)
