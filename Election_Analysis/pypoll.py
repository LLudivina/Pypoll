# the data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes

import csv

import os

#cd "C:\Users\calla\Desktop\bootcamp\challenges file\Pypoll\Election_Analysis"
#note:if file is not found, make sure the current directory has a folder called "resources"
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

# open the election results and read the file
#with open(file_to_load) as election_data:

# To do: perform analysis
    #print(election_data)  
    
# close the file
#election_data.close()

# create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1.initialize a total vote counter
total_votes = 0

#candidate options
candidate_options = []
#1. declare the empty dicrectory
candidate_votes = {}

# using the open() function with the "w" mode we will write data to the file
#with open(file_to_save, "w") as txt_file:

#write some data to the file
    #txt_file.write("Counties in the Election\n-----------\nArapahoe\nDenver\nJefferson")
  
#close the file
#txt_file.close()

#track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

#Open the election results and read the file
with open(file_to_load) as election_data:
    #save the results to our text file
    with open(file_to_save, "w") as txt_file:
        #To do: read and analyze the data here
        file_reader = csv.reader(election_data)

        #Read the header row
        headers = next(file_reader)

        #print each row in the CSV file
        for row in file_reader: 
            #2.add to the total vote count
            total_votes +=1
        
            #Print the candidate name from each row
            candidate_name = row[2]

            #add the candidate name to the candidate list
            #candidate-options.append(candidate_name)

            #if the candidate does not match any existing candidate..
            if candidate_name not in candidate_options:
                #Add it to the list of candidates
                candidate_options.append(candidate_name)

                #2 Begin tracking that candidate's vote count
                candidate_votes[candidate_name] = 0
                #print("** New Candidate ", candidate_name)

            #Add a vote to that candidate's count
            candidate_votes[candidate_name] +=1
        
        # Print the final vote count to the terminal.
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

        print(election_results, end="")
        
        # Save the final vote count to the text file.
        txt_file.write(election_results)     

        #Determine the percentage of votes for each candidate by looping through the counts
        #print("***",candidate_name,"***")
        #1. iterate through the candidate list
        for candidate_name in candidate_votes:
            #2 Retrieve vote count of a candidate
            votes =  candidate_votes[candidate_name]
            #3.Calculate the percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100
            #4.print the candidate name and percentage of votes to the terminal
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            #print each candidate, their voter count, and percentage to the terminal
            print(candidate_results)

            #save the cancidate results to our text file
            txt_file.write(candidate_results)

            #Determine wining vote count, winning percentage, and candiate
            if(votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage    
                
        #3. print the total votes
        #print(row)
        #print("TOTAL VOTES = ", total_votes)

        #print the candidate list
        #print(candidate_options)
        #print the winning candidates' results to the terminal
        winning_candidate_summary = (
            f"------------------------\n"
            f"winner: {winning_candidate}\n"
            f"winning vote count: {winning_count:,}\n"
            f"winning percentage: {winning_percentage:.1f}%\n"
            f"---------------------------\n")

        #print(candidate_votes)
        print(winning_candidate_summary)

        #save the winning candidate's results to the text file
        txt_file.write(winning_candidate_summary)






    
  
