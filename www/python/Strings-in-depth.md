# String in-depth
Lets try to learn some useful function in the str class
# Universal newlines support
In windows new lines should be represented by the carriage return at new line couplet \r\n. In linux it is simply \n

Operating System| New line character
---|---
Windows| \r\n
Linux| \n

In python new line character is **\n**
```python
>>> msg="Hello\nWorld"
>>> print(msg)
Hello
World
```
# Length of a String
We can use python built in function **len()** to find Length of a String
```python
>>> len("HelloHowAreyou")
14
```
# Concatenation using +
```python
>>> "Hello" + "World" + "Python"
'HelloWorldPython'
```
# Concatenation using join
Join is a method on str which takes a collection of strings as an argument and produces a new string by inserting a separator between each of them.
```python
>>> ",".join(["Hello","World","Python"])
'Hello,World,Python'
```
Join using empty
```python
>>> "".join(["Hello","World","Python"])
'HelloWorldPython'
```
# Split Strings
Strings can be splitted using split function
```python
>>> "Hello,World,Python".split(",")
['Hello', 'World', 'Python']
```
# Partition
It divides a string into three sections, the part before the separator, the separator itself, and the part after the separator.
The partition() method divides a string into three around a separator: prefix, separator, suffix
```python
>>> source,seperator,destination="LondonToNewyork".partition("To")   
>>> source                                                           
'London'                                                             
>>> seperator                                                        
'To'                                                                 
>>> destination                                                      
'Newyork'                                      
```
Using underscore
```python
>>> source,_,destination="LondonToNewyork".partition("To")               
>>> source                                                               
'London'                                                                 
>>> destination                                                          
'Newyork'                                                                
>>> _                                                                    
'To'                                                                     
```
Note: **_** underscore variable is for unused or dummy values
# Replacement using format function
Token Replacement in python can be done using format function
```python
>>> "The age of {0} is {1} years".format("sun",4.6e9)
'The age of sun is 4600000000.0 years'
```
You can repeat the index
```python
>>> "The age of {0} is {1} years.{0} is very old".format("sun",4.6e9)
'The age of sun is 4600000000.0 years.sun is very old'
```
Keyword arguments
```python
>>> "The age of {name} is {age} years".format(name="sun",age=4.6e9)
'The age of sun is 4600000000.0 years'
```
You can pass tuple or list
```python
>>> "The age of {position[0]} is {position[1]} years".format(position=["sun",4.6e9])
'The age of sun is 4600000000.0 years'
```
Pass object
```python
>>> import math
>>> "Math constants pi={m.pi}, Euler's number e={m.e}".format(m=math)
"Math constants pi=3.141592653589793, Euler's number e=2.718281828459045"
```


# [Python Home](index.html)
