# Bytes
Bytes in python are sequence of single **byte**.  They are used for raw binary data and fixed with single byte character encodings such as ASCII.

# Create a byte object
```python
>>> x=b'some bytes'
>>> x
b'some bytes'
>>> x.split()
[b'some', b'bytes']
```
# byte function
 ```pyton
 >>> x = bytes('Hello Python', 'utf8')
 >>> print(x)
 b'Hello Python'
 ```
# Note
It's crucial to understand since files and network resources such as HTTP responses are transmitted as byte streams whereas we prefer to work with the convenience of Unicode strings
#[Python Home](index.html)
