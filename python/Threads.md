# Threads
A Thread or a Thread of Execution is defined in computer science as the smallest unit that can be scheduled in an operating system
- Threads are usually contained in processes
- More than one thread can exist within the same process.
- These threads share the memory and the state of the process. In other words: They share the code or instructions and the values of its variables.

There are two different kind of threads:
- Kernel threads Threads are part of the operating system
- User-space Threads are not implemented in the kernel.

# User-space Threads
ser-space threads can be seen as an extension of the function concept of a programming language. So a thread user-space thread is similar to a function or procedure call. But there are differences to regular functions, especially the return behaviour.

# Python Threads
In python we create threads using **threading** module.
Note: The thread module has been considered as "deprecated" for quite a long time. Users have been encouraged to use the threading module instead. So,in Python 3 the module "thread" is not available anymore. But that's not really true: It has been renamed to "\_thread" for backwards incompatibilities in Python3.  

# Threading module
Simple python program runs in a single thread
```python
import threading
if __name__ == "__main__":
     print("Hello world")
     print(threading.active_count()) #  Returns the number of thread objects that are active.
     print(threading.current_thread()) # Returns the current thread
     print (threading.enumerate()) #  Returns a list of all thread objects that are currently active.
```
```
Hello world
1
<_MainThread(MainThread, started 3780)>
[<_MainThread(MainThread, started 3780)>]

```
Simple thread
```python
import time
from threading import  Thread

def print_a():
    for i in range(10):
        print("A")
        time.sleep(0.5)



if __name__ == "__main__":
    t = Thread(target=print_a)  # run print_a function
    t.start()  # start new thread and main thread proceeds

print("Main exited")

```
```
A
Main exited
A
A
A
A
```
**Note:Main thread exited before the child thread exited**

Make main thread to wait till the spawned child thread finishes

```python
import time
from threading import  Thread

def print_a():
    for i in range(5):
        print("A")
        time.sleep(0.5)



if __name__ == "__main__":
    t = Thread(target=print_a)  # run print_a function
    t.start()  # start new thread and main thread proceeds
    t.join() # wait for thread to terminate
print("Main exited")

```
```
A
A
A
A
A
Main exited
```
Create two threads and make main thread to wait until they are finished
```python
import time
from threading import  Thread

def print_a():
    for i in range(5):
        print("A")
        time.sleep(0.5)

def print_b():
    for i in range(5):
        print("B")
        time.sleep(0.5)

if __name__ == "__main__":
    t1= Thread(target=print_a)
    t2= Thread(target=print_b)
    t1.start()
    t2.start()
    # Make main thread to wait till the child threads finished
    t1.join()
    t2.join()

print("Main exited")
```
```
A
B
B
A
B
A
B
A
A
B
Main exited
```
### [index](index.html)
