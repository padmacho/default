# Process JSON text
Lets process the JSON text that represent student information.
# Student JSON
Below student object has attributes id, name and marks
```js
{
  "id": 1001,
  "name": "Dora",
  "marks": 90
}
```
# Read json file from disk
Read JSON file from disk and pass file object to **json.load** function
```Python
import json

with open('student.json') as file_obj:
    # read json file from disk and parse to create a dictionary object
    student_dict = json.load(file_obj)

```
# Read name value pairs
Read student attribute name,id,marks
```Python
>>> student_dict['name']    
'Dora'                      
>>> student_dict['id']      
1001                        
>>> student_dict['marks']   
90                          
```
# Student json file with address
Sudent object which contains address object
```js
{
  "id": 1001,
  "name": "Dora",
  "marks": 90,
  "address": {
    "street": "383 Madison Ave, New York",
    "pincode": 10017
  }
}
```
# Reading more fields
```Python
>>> student_dict["address"] # Read student address
{'street': '383 Madison Ave, New York', 'pincode': 10017}
>>> student_dict['address']['street']  # Read street number
'383 Madison Ave, New York'
```
# Student json with address and subjects
Studnet with address and subject object
```js
{
  "id": 1001,
  "name": "Dora",
  "marks": 90,
  "address": {
    "street": "383 Madison Ave, New York",
    "pincode": 10017
  },
  "subjects": [
    "english",
    "maths",
    "science"
  ]
}
```
# Reading list from JSON
Read subjects
```Python
>>> student_dict['subjects']
['english', 'maths', 'science']
>>> student_dict['subjects'][0]
'english'
```
# Source Files
- [student.json](student.json)
- [student_address.json](student_address.json)
- [student_address_subjects.json](student_address_subjects.json)
- [JSON.py](JSON.py)

# [Python Home](index.html#JSON)
