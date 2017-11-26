# Range
 It generates a list of numbers, which is generally used to iterate over with for loops.
```Python
range(stop) # Simple form
range([start], stop[, step]) # Actual form
```
- start: Starting number of the sequence. **Note** start is optional
- stop: Generate numbers up to, **but not** including this number.
- step: Difference between each number in the sequence.

# Example
```Python
>>> range(5)  # Create a sequence of elements with stop 5       
range(0, 5)         
>>> range(-5) # elements at stop -5       
range(0, -5)        
>>> type(range(5)) # range is a separate type
<class 'range'>     
>>> list(range(5))  # Convert range to list
[0, 1, 2, 3, 4]
>>> list(range(0,10,2)) # Provide step to produce even numbers
[0, 2, 4, 6, 8]
>>> list(range(1,10,2)) # Provide step to produce odd numbers
[1, 3, 5, 7, 9]     
```
# Range with for loop
```Python
# Print 0 to 9 using for loop
>>> for i in range(10):
...     print(i,end=" ")
...
0 1 2 3 4 5 6 7 8 9
```
# [Python Home](index.html#Range)
