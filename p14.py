import pandas as pd
# Read the csv file into a DataFrame using pd.read_csv()
df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")
# Display the first 5 rows of the DataFrame using head()
print("First 5 Rows: ")
print(df.head(5))
# Display the last 5 rows of the DataFrame using tail()
print("\nLast 5 Rows: ")
print(df.tail(5)) 
#
