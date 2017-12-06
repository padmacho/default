import numpy as np
import pandas as pd

# List of students with marks in mathematics subject
students = [(100, 'Alex', 60, 'M'), (101, 'Mike', 99, 'M'), (102, 'Dora', 100, 'F'), (103, 'Chitki', 40, 'F')]
# Create a data frame from  list of tuples
df = pd.DataFrame.from_records(students, columns=['id', 'name', 'marks', 'gender'])

# Grouping
# Group student by Gender column
grouped_data = df.groupby('gender')

# Know the type of grouped data
type(grouped_data)

# iterate through group by data frame
for gender, group_df in grouped_data:
    print(gender)
    print(group_df)

# Aggregate operations

# Get maximum mark in male
grouped_data.get_group('M')['marks'].max()

# Using aggregate function and pass numpy max function as argument
grouped_data.get_group('M')['marks'].agg(np.max)

# Transform
# Lets add one mark to all the students
df['marks'] = df['marks'] + 1


# define an increment function
def increment(marks):
    return marks + 1


# Apply the increment method to marks column
df['marks'].transform(increment)


# filter
# remove students who are having less than 70 marks
def remove_student(marks):
    if marks < 70:
        return False
    else:
        return True


# apply the filter
df['marks'].filter(remove_student)
