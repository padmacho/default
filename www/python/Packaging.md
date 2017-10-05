# Packaging
Packaging and distributing your Python code can be complex and sometimes confusing task, especially if your projects have lots of dependencies or involve components more exotic than straight Python code


## distutils
The distutils module allows you to write a simple Python script, which knows how to install your Python modules into any Python installation

Lets create a simple super_calc module and distribute it to friend for using

super_calc.py
```python
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
```
setup.py
```python
from distutils.core import setup

setup(
    name='super_calc',
    version='1.0',
    py_modules=['super_calc'],

    # metadata
    author='mario',
    author_email='mario@superman.com',
    description='A module for really doing large mathematical operations.',
    license='Public domain',
    keywords='example',
)
```
Install the module in local python installation
```bash
python setup.py install
```
Move to any directory and start using the module.
```bash
dragon@AIRAVATH D:\                                                                              
> python                                                                                         
Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32        
Type "help", "copyright", "credits" or "license" for more information.                           
>>> import super_calc                                                                            
>>> super_calc.add(1,2)                                                                          
3                                                                                                
>>>                                                                                              
```

## distribute python module
Lets distribute super_calc module in the form of zip so that others start using it
```bash
>python setup.py sdist --format zip
creating 'dist\super_calc-1.0.zip' and adding 'super_calc-1.0' to it
adding 'super_calc-1.0\PKG-INFO'
adding 'super_calc-1.0\setup.py'
adding 'super_calc-1.0\super_calc.py'
removing 'super_calc-1.0' (and everything under it)
```
The above command does source distribution
## Use the distributed module
Unzip the source distributed python module
```bash
jar -xvf super_calc-1.0.zip
 inflated: super_calc-1.0/PKG-INFO
 inflated: super_calc-1.0/setup.py
 inflated: super_calc-1.0/super_calc.py
```
install the module
```bash
dragon@AIRAVATH D:\work\git-local-repo\pythontutorial\distutils_demo\dist\test\super_calc-1.0
> python setup.py install                                                                     
running install                                                                               
running build                                                                                 
running build_py                                                                              
creating build                                                                                
creating build\lib                                                                            
copying super_calc.py -> build\lib                                                            
running install_lib                                                                           
running install_egg_info                                                                      
Removing D:\Python36-32\Lib\site-packages\super_calc-1.0-py3.6.egg-info                       
Writing D:\Python36-32\Lib\site-packages\super_calc-1.0-py3.6.egg-info                        
```
import the module and use it
```bash
dragon@AIRAVATH D:\
> python
Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import super_calc
>>> print(super_calc.__file__)
D:\Python36-32\lib\site-packages\super_calc.py
>>>

```
## Make your library available Global


## Get help of distutils
```bash
> python setup.py --help
Common commands: (see '--help-commands' for more)

  setup.py build      will build the package underneath 'build/'
  setup.py install    will install the package

Global options:
  --verbose (-v)      run verbosely (default)
  --quiet (-q)        run quietly (turns verbosity off)
  --dry-run (-n)      dont actually do anything
  --help (-h)         show detailed help message
  --no-user-cfg       ignore pydistutils.cfg in your home directory
  --command-packages  list of packages that provide distutils commands
```
## Installing third party modules into python installation
There are three ways to do it  
- distutils
- easy_install
- pip

### distutils
As covered in the previous section use setup.py to install the module
```bash
python setup.py install
```
### easy_install
It search for packages in a central repository, the Python package index or PyPI, also known by the nickname cheeseshop, and then download and install them along with their dependencies.
You can browse the cheeseshop at pypi.python.org/pypi

Install requests module using easy_install
```bash
dragon@AIRAVATH D:\work\git-local-repo\pythontutorial\distutils_demo
> easy_install requests
Searching for requests
Reading https://pypi.python.org/simple/requests/
Downloading https://pypi.python.org/packages/2c/b5/2b6e8ef8dd18203b6399e9f28c7d54f6de7b7549853fe36d575bd31e29a7/requests-2.18.1.tar.gz#md5=40f723ed01dddeaf990d0609d073f021
Best match: requests 2.18.1
Processing requests-2.18.1.tar.gz
Writing C:\Users\dragon\AppData\Local\Temp\easy_install-rlcvy8u5\requests-2.18.1\setup.cfg
Running requests-2.18.1\setup.py -q bdist_egg --dist-dir C:\Users\dragon\AppData\Local\Temp\easy_install-rlcvy8u5\requests-2.18.1\egg-dist-tmp-9il7xpbl
warning: no files found matching 'NOTICE'
```
### pip
Install requests module using pip
```bash
dragon@AIRAVATH D:\work\git-local-repo\pythontutorial\distutils_demo                                     
> pip install  requests                                                                                  
Requirement already satisfied: requests in d:\python36-32\lib\site-packages\requests-2.18.1-py3.6.egg    
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in d:\python36-32\lib\site-packages\chardet-3.0.4-py
3.6.egg (from requests)                                                                                  
Requirement already satisfied: idna<2.6,>=2.5 in d:\python36-32\lib\site-packages\idna-2.5-py3.6.egg (fro
m requests)                                                                                              
Requirement already satisfied: urllib3<1.22,>=1.21.1 in d:\python36-32\lib\site-packages\urllib3-1.21.1-p
y3.6.egg (from requests)                                                                                 
Requirement already satisfied: certifi>=2017.4.17 in d:\python36-32\lib\site-packages\certifi-2017.4.17-p
```

### [index](index.html)
