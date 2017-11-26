import pandas as pd

# Read only five rows from csv file
df = pd.read_csv(r"D:\work\pandas-fundamentals\02\demos\demos\collection-master\artwork_data.csv", nrows=5)

# Set index column as id
df = pd.read_csv(r"D:\work\pandas-fundamentals\02\demos\demos\collection-master\artwork_data.csv", nrows=5,
                 index_col='id')
# Limit number of columns
df = pd.read_csv(r"D:\work\pandas-fundamentals\02\demos\demos\collection-master\artwork_data.csv", nrows=5,
                 index_col='id', usecols=['id', 'artist'])

COLS_TO_USE = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']

df = pd.read_csv(r"D:\work\pandas-fundamentals\02\demos\demos\collection-master\artwork_data.csv", nrows=5,
                 index_col='id', usecols=COLS_TO_USE)

# Drop the row limit
df = pd.read_csv(r"D:\work\pandas-fundamentals\02\demos\demos\collection-master\artwork_data.csv",
                 index_col='id', usecols=COLS_TO_USE)

# Write data frame to pickle format
df.to_pickle(r"D:\work\pandas-fundamentals\02\demos\demos\collection-master\artwork_data_frame.pickel")
