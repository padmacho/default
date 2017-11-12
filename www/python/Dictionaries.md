# Dictionaries
 A dictionary **maps keys to values** and in some languages it is known as an associative array.
```python
{k1:v1,k2:v2}
```
Where k1,k2 are **keys** and v1,v2 are **values**
# Create a dictionary
```python
>>> students={"bob":90,"tom":50,"ram":70} # Create a dictionary
```
# Read a element in dictionary using key
```python    
>>> students["ram"] # access by key                          
70       
```
# Add a element in dictionary
```python                                     
>>> students["dora"]=30 # adds a new element in dictionary
```
# Update an element in dictionary
if **key** is not available a new key, value pair is added else **value**  is updated
```python
>>> students["dora"]=40
>>> students
{'bob': 90, 'tom': 50, 'ram': 70, 'dora': 40}
```
# Remove an element in dictionary
Remove an element with key **bob**
```python
>>> del students["bob"]
```
# Empty all elements in dictionary
```python
>>> students={"bob":90,"tom":50,"ram":70}
>>> del students
```
# iterate through elements in dictionary
```python
>>> students={"bob":90,"tom":50,"ram":70}
>>> for key in students:
...  print(key,students[key])
...
bob 90
tom 50
ram 70
```
Note: **key** is not a key word

**items()** method return all the elements in key,value pair
```python
>>> for key,value in students.items():
...  print(key,value)
...
bob 90
tom 50
ram 70
```
# Note
- The entries in dictionary are not stored in any particular order

# [Python Home](index.html#Dictionaries)
