import pandas as pd
 
input = "Finished_matches.csv"
output = "Unique_finished_matches.csv"
 
## read csv; index_col=False will remove the index to prevent a read of index col
df = pd.read_csv(input,index_col=False)
 
## df.drop_duplicates() = Selecting distinct values in a column of a SQL table, translated to Python's pandas.
data = df.drop_duplicates()
 
## write back out as copy so we don't disturb original raw data; don't write index col
data.to_csv(output, index=False)
