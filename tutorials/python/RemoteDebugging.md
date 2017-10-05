# Remote debugging python application
Remote debug a python application using rpdb module
## install rpbd module using pip
```cmd
dragon@AIRAVATH D:\work\git-local-repo\pythontutorial\distutils_demo
> pip install rpdb
Collecting rpdb
  Downloading rpdb-0.1.6.tar.gz
Installing collected packages: rpdb
  Running setup.py install for rpdb ... done
Successfully installed rpdb-0.1.6
```
## import rpdb in your code
```python
def add(x, y):
    import rpdb;rpdb.set_trace()
    return x + y

if __name__ == "__main__":
    print(add(10, 20))

```
## Run your python application
Run the application as normal python code
```cmd
dragon@AIRAVATH D:\work\git-local-repo\pythontutorial\pdb
> python calc.py
pdb is running on 127.0.0.1:4444
```
## Connect to debug server
Connect to debug server using telnet
```cmd
>telnet localhost 4444
 d:\work\git-local-repo\pythontutorial\pdb\calc.py(3)add()
-> return x + y
(Pdb)
```
If you are running python application on remote host. Replace local host with hostname

### [index](index.html)
