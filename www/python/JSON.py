import json

with open('student.json') as file_obj:
    # read json file from disk and parse to create a dictionary object
    student_dict = json.load(file_obj)

with open('student_address.json') as file_obj:
    # read json file from disk and parse to create a dictionary object
    student_dict = json.load(file_obj)

with open('student_address_subjects.json') as file_obj:
    # read json file from disk and parse to create a dictionary object
    student_dict = json.load(file_obj)
