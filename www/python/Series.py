import pandas as pd

# Create series of students with their ids using lists
se = pd.Series(data=['Alex', 'Nelly', 'Mike'], index=[100, 101, 102])
print(se)

# Create a series from students dict
se = pd.Series(data={100: 'Alex', 101: 'Nelly', 102: 'Mike'})
print(se)

# Access date using index
# Access first element with index
se[100]

# Slicing
# Retrieve all elements
se[:]

# Retrieve first element
se[0:1]

# Change Alex to Alexander
se[100] = 'Alexander'
print(se[100])

# delete an element form series
del se[100]
print(se[:])

# delete the whole series
del se
