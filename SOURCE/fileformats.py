import pandas as pd
import csv
# Path to your CSV file

# Path to your CSV file
file_path = r"C:\Users\rajas\Downloads\archive\gifts_age.csv"
#df = pd.read_csv(file_path, header=1) 
# Open the CSV file
#print(df)
with open(file_path, "r") as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    rows = list(csv_reader)  # Read all rows at once
    # Read each row in the CSV file
#    for row in csv_reader:
#        print(row)  # Do whatever you need with the row data
#  Convert the rows into a Pandas DataFrame
dataframe = pd.DataFrame(rows)
print(dataframe)
columns_to_sum = dataframe.columns[1:]
print(columns_to_sum)
print(dataframe)



