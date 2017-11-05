# Installation on Linux
Recent versions of Ubuntu Linux include Python 3 out of the box, so no installation is required.By default both Python 2 and Python 3 are already installed on Linux

# Know python version
In Linux **python** is for Python2.x version and **python3** is for Python3.x version
```bash
vagrant@python-m1:~$ python --version
Python 2.7.12
```
```bash
vagrant@python-m1:~$ python3 --version
Python 3.5.2
```
# Install from source code
Python can be installed from source
- Download source code
- Unzip the zipped archive
- Configure the build with the install location, where to find any libraries it needs, etc.
- Compile the source code
- Test the python
- Install the python
```bash
$ wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0a2.tgz
$ tar -zxvf Python-3.7.0a2.tgz
$ cd Python-3.7.0a2
$ ./configure
$ make
$ make test
$ make install
```

# [Python Home](index.html#InstallLinux)
