# Expression
Expression  is the most basic kind of programming instruction in the language. Expressions consist of **values** (such as 4) and **operators** (such as +), and they can always **evaluate** (that is,
reduce) down to a single value
```python
>>> 4+4
8
```
# Operators
Operator | Operation | Example | Result | Remarks
---|---|---|---|---
\**|Exponent|3**2|9|Highest Precedence
%| Modulus/remainder| 5%2|1|
//| Integer division/floored quotient| 5//2|2
/|Divison|5/2|2.5
\*|Multiplication|2*3|6
-|Subtraction|5-2|3
+|Addition|5+2|7

# Operators Precedence
The order of operations (also called precedence) of Python math operators is similar to that of mathematics. The ** operator is evaluated first; the \*, /, //, and % operators are evaluated next, from left to right; and the \+ and - operators are evaluated last (also from left to right).

# Parentheses to override precedence
You can use parentheses to override the usual precedence
```bash
>>> 2+3*6
20
>>> (2+3) * 6
30
```
# Invalid Syntax
```python
>>> 2+*3
  File "<stdin>", line 1
    2+*3
      ^
SyntaxError: invalid syntax
```
You can always test to see whether an instruction works by typing it into the interactive shell. Don’t worry about breaking the computer: The worst thing that could happen is that Python responds with an error message. Professional software developers get error messages while writing code all the time.:)
# [Python Home] (index.html)
