# Conditional statements
Conditional statements allow us to branch execution based on the value of an expression.
```python
if expr:
  print("Exp is True")
```
expr is converted to bool  as if by the bool() Constructor
# Video
<div style="position:relative;height:0;padding-bottom:56.25%"><iframe src="https://www.youtube.com/embed/B_sw2hCdgOY?rel=0?ecver=2" width="640" height="360" frameborder="0" gesture="media" style="position:absolute;width:100%;height:100%;left:0" allowfullscreen></iframe></div>

# if
```python
>>> if True:                        
...     print("It is true!")        
...                                 
It is true!                         
>>> if False:                       
...     print("It is not true")     
...                                 
>>> if bool("hello"):               
...     print("Hello .. Thank you")
...                                 
Hello .. Thank you
>>> if bool(""):                      
...     print("Empty is not true")    
...                                   
>>>
```

# if and else
```python
>>> i=10
>>> if(i==11):
...     print("It is  11")
... else:
...     print("It is 10")
...
It is 10
```
Nested if inside else
```python
>>> i=10
>>> if(i==11):                     
...     print("i is 11")           
... else:                          
...     if(i==9):                  
...         print("i is 9")        
...     else:                      
...         print("i may be 10")   
...
i may be 10                                
```
Whenever you find yourself with an else block containing a nested if statement , you should consider instead using Python's elif keyword, which is a combined else/if
# elif (else/if)
```python
>>> if(i==11):                 
...     print("i is 11")       
... elif(i==9):                
...     print("i is 9")        
... else:                      
...     print("i may be 10")   
...                            
i may be 10
```
# effect of bool
The **expression** need not to be boolean python explicity converts the expression to boolean
```python
if expr:
  print("Exp is True")
```
```python
if bool(expr):
  print("Exp is True")
```
```python
>>> if True:                                 
...     print("I am true")                   
...                                          
I am true                                    
>>> if "1":                                  
...     print("I am also true")              
...                                          
I am also true                               
>>> if "":                                   
...     print("I am not true")               
...                                          
>>> if "False":                              
...     print("This is not an empty String")
...                                          
This is not an empty String                  
>>>                                          
```
# Conditional expression
It is similar to ternary operator **?** in other languages
```python
a if expression else b
```
if **expression** is true a is returned else b is returned
```python
>>> a = 10                   
>>> b = 11                   
>>> print(a if a > b else b)
11                           
```

# [Python Home](index.html#Conditional-Statements)
