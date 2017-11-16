# Tuple
 A tuple is similar to a list. The difference between the two is that we **cannot change** the elements of a tuple once it is created whereas in a list, elements can be changed.
# Create tuple
```python
>>> tu=(1,2,3,4,5)
>>> tu
(1, 2, 3, 4, 5)
```
# Tuple vs List
 Tuple| List
 ---|---
immutable -Once created contents cannot be changed| mutable -contents can be changed
Generally use tuple for heterogeneous (different) datatypes|list for homogeneous (similar) datatypes.
Example: date_of_birth=(10,"aug",2000)| Example: heights=[150,160,170]
Iteration is slightly faster than list| relatively slower than tuple
```python
>>> li=[1,2,3,4]
>>> li.append(5)
>>> li                                                     
[1, 2, 3, 4, 5]
```
```python                                       
>>> tu=(1,2,3,4)                                           
>>> tu.append(5) # Once created they cannot be changed                                          
Traceback (most recent call last):                         
  File "<stdin>", line 1, in <module>                      
AttributeError: 'tuple' object has no attribute 'append'   
>>>                                                         
```
# Accessing elements
Elements can be accessed with index
```python
>>> tu=(10,"aug",2000)
>>> tu[0]              
10                     
```
Negative Index is also supported
```python
>>> tu[-1]
2000
```
# Slicing or sub tuple
We can access a range of items in a tuple by using the slicing operator - colon ":".
```python

```
