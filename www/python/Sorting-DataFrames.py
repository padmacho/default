import pandas as pd

# List of student tuples with id,name and marks
students = [(102, 'Dora', 90), (103, 'Hulk', 80),
            (104, 'Hanuma', 99), (105, 'Hulk', 40),
            (106, 'Spiderman', 10), (107, 'Ninja', 11),
            (108, 'Somu', 0), (109, 'Alex', 100),
            (110, 'Buddu', 0)]
# Create a data frame from records
df = pd.DataFrame.from_records(students)

# Set column names
df.columns = ['id', 'name', 'marks']

# find occurrence of values
df['marks'].value_counts()

# Sort marks column - Default order is increasing
df['marks'].sort_values()

# Get top 5 values in sorted column
df['marks'].sort_values().head()

# Get bottom 5 values in sorted column
df['marks'].sort_values().tail()
