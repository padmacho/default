# Reading command line arguments
sys.argv is a **list** which contains the command-line arguments passed to script
- First argument is the script name

```Python
import sys
if __name__=="__main__":
    print("Arguments are: ",sys.argv)
    print("Length: ",len(sys.argv))
    print("First argument is script name: ",sys.argv[0])
```
```bash
$ python reading-arguments.py
Arguments are:  ['reading-arguments.py']
Length:  1
First argument is script name:  reading-arguments.py
```
```bash
$ python reading-arguments.py argument1
Arguments are:  ['reading-arguments.py', 'argument1']
Length:  2
First argument is script name:  reading-arguments.py
```
# Starting a  simple python web server
Python has http server module . The module can be executed and it by default it binds to **8000** on all the Ethernet interfaces.

This will expose current working directory

```bash
$ python -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```
#[Git Home](index.html)
