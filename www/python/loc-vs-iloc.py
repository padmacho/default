import pandas as pd

# List of student tuples with id,name and marks
students = [(1, 'Dora', 90), (2, 'Hulk', 80), (3, 'Hanuma', 99), (4, 'Hulk', 40)]
# Create a data frame from records
df = pd.DataFrame.from_records(students)

# Set column names
df.columns = ['id', 'name', 'marks']
# Set id column as index
df.set_index('id', inplace=True)

# Select name column
df['name']
# other way of selecting name column but don't use it
df.name

# Select unique elements in  name column
pd.unique(df['name'])

# Filter columns that has name as 'Hulk'
df['name'] == 'Hulk'

# Number of elements in a column
len(df['name'])

# occurrence of each element in the column
df['name'].value_counts()

# Occurrence of Hulk in the column
s = df['name'].value_counts()
s['Hulk']

# loc vs iloc
# List of student tuples with id,name and marks
students = [(102, 'Dora', 90), (103, 'Hulk', 80), (104, 'Hanuma', 99), (105, 'Hulk', 40)]
# Create a data frame from records
df = pd.DataFrame.from_records(students)

# Set column names
df.columns = ['id', 'name', 'marks']
# Set id column as index
df.set_index('id', inplace=True)

# Get student name with id 102
df.loc[102, 'name']

# Get all columns for the row id 102
df.loc[102, :]

# Get all rows that has name as 'Hulk'
df.loc[df['name'] == 'Hulk', :]

# Get element in first row and first column
df.iloc[0, 0]

# Get all elements in second column
df.iloc[:, 1]

# Get first two rows and two columns
df.iloc[0:2, 0:2]

# Arithmetic operation on data frames
# add one grace mark to every student
df['marks'] = df['marks'] + 1

# Sort marks - Default order is ascending
df['marks'].sort_values()
