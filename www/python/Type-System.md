# Type System
## Language Matrix
Category |Static |Dynamic
---|---|---
Strong |C,C++,Java, | **Python**, Ruby
Weak| None | JavaScript, Perl

- *Dynamic typing* - Dynamically typed programming languages do type checking at *run-time*
- *Static Typing* - Statically typed programming languages do type checking (the process of verifying and enforcing the constraints of types) at *compile-time*
- *Strong Typing* - Common definition is that the language will not in general **implicitly** convert objects between types.
- *Weak Typing* - The type of a value depends on how it is used, data types are defined at runtime or the context in which they are used.
Python can be characterized as having a dynamic and strong type system.
## Dynamic Type system
In a dynamic type system objects types are only **resolved at runtime.**
```python
def add(x, y):
    print(x + y)
add(1, 2) # add int
add(10.1, 11.2) # add float
add("abc", "xyz")# add string
add([1, 2], [3, 4]) # add list
```
```bash
3
21.299999999999997
abcxyz
[1, 2, 3, 4]
```
## Strong type system
Common definition is that the language will not in general **implicitly** convert objects between types
```python
def add(x, y):
    print(x + y)
add("This is string", 10)  # This leads to error     
```
```bash
print(x + y)
TypeError: must be str, not int
```
**Note**: The exception being the conversion to bool used for if statements and while-loop predicates.

## Object references (variables) has no types
```python
x = "abc"  # x is binded to string
print(x)
x = 1  # x can be rebinded to integer
print(x)
```
```bash
abc
1
```
# [Python Home](index.html#Type-System)
