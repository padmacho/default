# REST
REST (REpresentational State Transfer) has emerged as the standard architectural design for web services and web APIs.
# Flask
Flask is a simple, yet very powerful Python web framework.
# Install Flask
Standard python distribution doesn't contain flask. Install flask using **pip**
```bash
PS D:\> pip install flask
Collecting flask
  Downloading Flask-0.12.2-py2.py3-none-any.whl (83kB)
    100% |████████████████████████████████| 92kB 166kB/s
```
# Hello World REST Service
The below service returns "Hello World" Text when user access it.
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```

# Execute the service
The script gets executed and embedded webserver bound to port 5000
```python
$ python rest_api_demo.py
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 415-348-367
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [02/Nov/2017 09:37:27] "GET / HTTP/1.1" 200 -
```

# Test the service  using CURL or Web browser
curl - cURL is a command line tool to browse web pages or consume http services
```bash
dragon@airavath:/$ curl  http://localhost:5000/
Hello, World!
```
Using Chrome browser
![Rest API](rest-api-screenshot.png)

# [Python Home](index.html)
