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

#print total num of all columns
num_cols = dataframe.shape[1]
print("Number of Columns : ", num_cols)

# Get column names from first row of the dataframe (assuming it is present) 
colnames = dataframe.iloc[0]       
# Remove this row from the dataframe
dataframe = dataframe[1:]                    
# Set the column names to be used in the dataframe
dataframe.columns = colnames 
# Print number of rows and columns in the dataframe
print("Number of Rows : ", dataframe.shape[0])

# total flowers  given by women aged between 25-34 years old
                                                   
flowers_women_aged_25_34 = dataframe[(dataframe['Age'] >= 25) & (dataframe['Age'] <= 34)]['Flowers'].sum()
print('Total Flowers Given By Women Aged Between 25 And 34 Years Old : ', flowers_women_aged_25_34)
# total number of men who gave flowers to women aged between 25-34 years old

