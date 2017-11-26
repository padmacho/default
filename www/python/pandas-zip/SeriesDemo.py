import numpy as np
import pandas as pd

# Create a numpy array
my_array = np.random.rand(3)

# Convert numpy array to series object
my_series = pd.Series(my_array)

# Read an element with index
print(my_series[0])

# Create own indexes
my_series = pd.Series(my_array, index=["First", "Second", "Third"])

# access element with our own index
print(my_series["First"])
