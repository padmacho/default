# Virtual Environment
A virtual environment is a light-weight, self-contained Python installation that users can create without needing administrator rights on their system

A Virtual Environment is a tool to keep the dependencies required by different projects in separate places, by creating virtual Python environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.
##  Create a virtual environment
venv module can be used to create a virtual environment
```bash
python3 -m venv DemoEnv
```
The above command creates a DemoEnv folder in current working directory and copies all the necessary binaries

## Activate the environment
Change to DemoEnv/Scripts
On Windows: Run activate.bat script in Scripts folder
```bash
activate.bat
```
On Linux:
```bash
source activate
```
## Made modifications to virtual environment
install requests module
```bash
pip install requests
```
The above command will install pip on only in your virtual environment
```python
>>> import requests
>>> print(requests.__file__)
D:\work\git-local-repo\pythontutorial\virtualenv\DemoEnv\lib\site-packages\requests\__init__.py
```

### [index](index.html)
