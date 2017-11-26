# Operations on DataFrame
Common operations on Data Frame
# Create data frame
```python
import pandas as pd
students=[(1,'Dora',90),(2,'Hulk',80),(3,'Hanuma',99),(4,'Spiderman',40)]
df=pd.DataFrame.from_records(students)
```
![Students-Data-Frame](Students-Data-Frame.PNG)
# Set columns and index
```Python
df.columns=['id','name','marks'] # Set column names
df.set_index('id',inplace=True) # Set id column as index
```
![Students-Data-Frame-Index-Column-Names](Students-Data-Frame-Index-Column-Names.PNG)



# Selecting column
# [Python Home](index.html#Operations-on-DataFrame)
