# Lists
A list is a value that contains multiple values in an ordered sequence. Lists are **mutable** in so far as the elements within them can be replaced or removed, and new elements can be inserted or appended. Lists are delimited by square brackets, and the items within the list separated by commas.

Elements are **zero** based index

List|P|Y|T|H|O|N
---|---|---|---|---|---|---
Index|0|1|2|3|4|5
Negative Index| -6|-5|-4|-3|-2|-1
# Create list
List with string elements
```python
>>> ["P","Y","T","H","O","N"]
['P', 'Y', 'T', 'H', 'O', 'N']
```
Integer List
```python
>>> [1,2,3] # integer list
[1, 2, 3]
```
String list
```pyhon
>>> ["apple","orange","banana"] # String list
['apple', 'orange', 'banana']
```
List can have elements with multiple data types
```python
>>> ["Apple",1,23.5,True]
['Apple', 1, 23.5, True]
```
List can have sub list with in them
```python
>>> co_ordinates=[[1,10],[2,11]]
>>> co_ordinates
[[1, 10], [2, 11]]
```
Note: **[1,10]** and **[2,11]** are sub list

## list function
list() function can be used to create a list
```python
>>> l=list()
>>> l.append(1)
>>> l.append(2)
>>> l
[1, 2]
>>> l.append([3,4]) # Notice element is added as list object not int  
>>> l                
[1, 2, [3, 4]]       
>>> l.extend([5,6])# each element got added as a separate element towards the end of the list.  
>>> l                
[1, 2, [3, 4], 5, 6]
>>> l.insert(0,0) # Insert element at particular index
>>> l
[0, 1, 2, [3, 4], 5, 6]                  
```
## Create list from Strings
```python
>>> list("Welcome to Python")
['W', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n']
```

# Getting values with Index
Elements in the list can be retrieved by using Index
```python
>>> l=["P","Y","T","H","O","N"]
>>> l[0] # Get first element
'P'
>>> l[5] # Get last element
'N'
>>> l[-1] # Get last element with index as -1
'N'
>>> l[-6] # Get first element using negative index
'P'
```
# Slicing lists
Get sub list from a given list .
General Syntax
```python
l[startIndex,endIndex]
```
Note: **endIndex** element will not be retrieved
```python
>>> l=["P","Y","T","H","O","N"]
>>> l[0:1] # Get element from index 0 till index 1. Note element with endIndex is ignored
['P']
>>> l[:] # Get all the elements
['P', 'Y', 'T', 'H', 'O', 'N']
>>> l[1:] # Get elements from index 1 to till end
['Y', 'T', 'H', 'O', 'N']
>>> l[:6] # Get elements from starting to index 6
['P', 'Y', 'T', 'H', 'O', 'N']
```

# Methods on lists
Most commonly used methods on the lists
## append
Appends elements to the list
```python
>>> x=[]            
>>> x.append(1)     
>>> x               
[1]                 
>>> x.append("two")
>>> x               
[1, 'two']          
>>>                 
```
## remove
Removes element from the list
- remove() method removes only the first occurrence of element in list
- del  operator removes  element with specific index in the list
Remove first occurrence of element in the list

```python
>>> l=[1,2,3,4,1]
>>> l.remove(1)
>>> l
[2, 3, 4, 1]
```
Remove element at specific index
```python
>>> l=[1,2,3,4,1]
>>> del l[4]
>>> l
[1, 2, 3, 4]
```

# length of a list
- len() function can be used to find number of elements in the list.
- \_\_len\_\_() method in the list class gives the length

```python
>>> l=["P","Y","T","H","O","N"]
>>> len(l)
6
>>> l.__len__() # call the method
6
```
# [Python Home](index.html)
