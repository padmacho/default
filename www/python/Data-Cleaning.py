import pandas as pd

# List of student tuples with id,name and marks
students = [(102, 'Dora', 90), (103, 'Hulk', 80),
            (104, 'Hanuma', 'a'), (105, 'Hulk',),
            (106, 'Buddu', -5), (107, 'Ninja',)]
# Create a data frame from records
df = pd.DataFrame.from_records(students)

# Set column names
df.columns = ['id', 'name', 'marks']

# Empty values
df['marks'].value_counts()

# Try to convert all the elements in the column to numeric
pd.to_numeric(df['marks'])

# Force pandas to convert String or None to NaN
pd.to_numeric(df['marks'], errors='coerce')

# Update the marks column
df['marks'] = pd.to_numeric(df['marks'], errors='coerce')

