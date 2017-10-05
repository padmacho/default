# Comprehensions
Comprehensions in Python are a concise syntax for describing lists, sets, or dictionaries in a declarative or functional style. This shorthand is readable and expressive meaning that comprehensions are very effective at communicating intent to human readers.
- List Comprehension

## List Comprehension
Lets construct a list from sting

**Syntax: [ expr(item) for item in iterable ]**
```python
sentence = "Python supports a concept called list comprehensions. It can be used to construct lists in a very natural, easy way, like a mathematician is used to do."
words = sentence.split()
print("words:", words)
char_count = [ len(word) for word in words]
print("characters count in word",char_count)
```
```
words: ['Python', 'supports', 'a', 'concept', 'called', 'list', 'comprehensions.', 'It', 'can', 'be', 'used', 'to', 'construct', 'lists', 'in', 'a', 'very', 'natural,', 'easy', 'way,', 'like', 'a', 'mathematician', 'is', 'used', 'to', 'do.']
characters count in word [6, 8, 1, 7, 6, 4, 15, 2, 3, 2, 4, 2, 9, 5, 2, 1, 4, 8, 4, 4, 4, 1, 13, 2, 4, 2, 3]
```

Find factorials of numbers from 1 to 10

```python
# find factorial of 1 t0 10

from math import factorial
f = [factorial(n) for n in range(10)]
print("Factorials of number from 1 to 10", f)
```
```
Factorials of number from 1 to 10 [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
```
## Set comprehensions
syntax: **{ expr(item) for item in iterable }**
similar to list with out duplicates
```python
# find factorial of 1 t0 10 and eliminate duplicates
from math import factorial
f = {factorial(n) for n in range(10)}
print("Factorials of number from 1 to 10 with out duplicates", f)
```
```
Factorials of number from 1 to 10 with out duplicates {40320, 1, 2, 362880, 6, 720, 5040, 24, 120}

```
## Dict comprehensions
Reverse a dictionary by makes values as keys and vice versa
```python
# Create a dicitonary by reversing keys and values

d = {"a":10, "b":20, "c":30}
print("Before", d)
d = {value:key for key, value in d.items()}
print("After", d)
```
```
Before {'a': 10, 'b': 20, 'c': 30}
After {10: 'a', 20: 'b', 30: 'c'}

```
**Don't cram too much complexity into comprehensions!**
## Filtering
syntax: **{ expr(item) for item in iterable if predicate(item) }**

```python
# ignore india  and china and count word length
sentence = "india china srilanka singapore"
words = sentence.split()
print("words:", words)
char_count = [ len(word) for word in words if word not in["india","china"] ]
print("characters count in word", char_count)
```
```
words: ['india', 'china', 'srilanka', 'singapore']
characters count in word [8, 9]

```
