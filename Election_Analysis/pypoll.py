# the data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes

import csv

import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

# open the election results and read the file
with open(file_to_load) as election_data:

# To do: perform analysis
    print(election_data)
    
# close the file
election_data.close()

# create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# using the open() function with the "w" mode we will write data to the file
with open(file_to_save, "w") as txt_file:

#write some data to the file
    txt_file.write("Counties in the Election\n-----------\nArapahoe\nDenver\nJefferson")
  
#close the file
txt_file.close()

#Open the election results and read the file
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)

#print each row in the CSV file
#for row in file_reader:
    #print(row)

#Read and print the header row
    headers = next(file_reader)

    print(headers)
