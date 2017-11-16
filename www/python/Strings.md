# String - Str
In Python, string is a sequence of Unicode characters. The sequence of characters in a Python string is **immutable** meaning that once you've constructed a string you can't modify its contents.
String literals in Python are delimited by quotes. You can use single quotes or double quotes.

**Default source encoding for python is UTF-8**
```python
s='This is a string'
s="This is also a string"
```
# Adjacent literal strings
These concatenated by the Python compiler into a single string
```python
>>> "Hello"  "World!"
'HelloWorld!'
>>>
```
# Concatenation
```python
>>> "Hello" + "World"
'HelloWorld'
```
# Repetition
Repeats the word for five
```python
>>> "Hello" * 5
'HelloHelloHelloHelloHello'
```

# Multiline strings
Multiline strings are delimited by three quote characters rather than one
```python
>>> """This is
... a multi line
... string"""
'This is \na multi line\nstring'
>>> m="This is \na multi line\nstring" # or embed new line character
>>> m
'This is \na multi line\nstring'
```
If you're working on Windows, you might be thinking that new lines should be represented by the carriage return at new line couplet \r\n. There's no need to do that with Python since Python 3 has a feature called universal newlines support, which translates from the simple \n to the native newline sequence for your platform on input and output. You can read more about universal newlines support in PEP278.
# Escape character

An escape character **\\** can be used to escape special characters like singe quote and double qoute in the string.

Escape character | Display as
---|---
\'| Single quote
\"| Double quote
\t| Tab
\n| New line or Line break
\\| Back slash

```python
>>> print("Bob's pen")
Bob's pen
```
```python
>>> print("My class mates are \nAlex\nMike\nNelly")     
My class mates are                                      
Alex                                                    
Mike                                                    
Nelly                                                   
```
# Raw Strings
 Raw strings don't support any **escapes** characters. To create a raw string, prefix the opening quote with a lowercase **r**

```python
>>> path=r"c:\users\mario\docs"
>>> path
'c:\\users\\mario\\docs'
```
# Convert other types to string
Convert integer , float to String

```python
>>> str(1)   
'1'          
>>> str(1.2)
'1.2'        
>>>          
```
# Read individual characters in the string
We can access individual characters using square brackets with an integer **zero-based** index.

```python
>>> s="mario"
>>> s[0]
'm'
>>> print(s[2])
r
>>> type(s[2])
<class 'str'>
```
Note: No separate char type called **characters** all are simpy **one element strings**

# Methods of String object

```python
>>> c="delhi"     
>>> c.capitalize() # strings are immutable
'Delhi'           
>>> c             
'delhi'
>>> x="hello world"
>>> x.split()
['hello', 'world']          
```
# UTF-8 characters
```python
>>> message="పైథాన్ కు స్వాగతం"
>>> message
'పైథాన్ కు స్వాగతం'
```
# [Python Home](index.html#Strings)
