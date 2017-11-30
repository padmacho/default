import pandas as pd

# List of student tuples in a class
students = [(1, 'Dora', 90), (2, 'Hulk', 80), (3, 'Hanuma', 99), (4, 'Spiderman', 40), (5, 'Bheem', 100),
            (6, 'Alex', 95), (7, 'Nelly', 80), (8, 'Hulk', 5)]
# Create data frame from students
df = pd.DataFrame.from_records(students)

# Set column names
df.columns = ['id', 'name', 'marks']

# Selecting a column
df['name']
# other way of access elements in column
# But this is not preferred way
df.name

# Selecting multiple column
df[['name', 'marks']]

# Gives number of occurrences of element in column
df['name'].value_counts()

# Get top 5 elements in a column
df['name'].head()

# Get bottom 5 elements in a column
df['name'].tail()

# find unique elements in column
pd.unique(df['name'])

# Adding a column named country
df = df.assign(country='India')

# Delete a column in data frame
del df['country']

print(df)

# Arithmetic operations on data frame
# Create a data frame
rectangles = [('rect1', 10, 20), ('rect2', 15, 20)]
df1 = pd.DataFrame.from_records(data=rectangles, columns=['id', 'length', 'breadth'], index=['id'])

# Create a area column
df1 = df1.assign(area=df1['length'] * df1['breadth'])

# Get maximum area
df1['area'].max()

# Get row with maximum area
df1.loc[df1['area'].idxmax(), :]
