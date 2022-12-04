# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis2.txt")

# Initialize a total vote counter.
total_votes = 0

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}
#candidate options
candidate_options = []
#1. declare the empty dicrectory
candidate_votes = {}

# Track the winning candidate, vote count and percentage
winning_county = 0
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""

#open the election results and read the file
with open(file_to_load) as election_data:

    #save the results to our text file
    with open(file_to_save, "w") as txt_file:
    #write data to the file
    #txt_file.write("hello")
        file_reader = csv.reader(election_data)
        
        # Read the header
        header = next(file_reader)

        # For each row in the CSV file.
        for row in file_reader:

            # Add to the total vote count
            total_votes = total_votes + 1

            # 3: Extract the county name from each row.
            county_name = row[1]
                
            #txt_file.write(county_name)

            # 4a: Write an if statement that checks that the county does not match any existing county in the county list.
            if county_name not in county_options:

                # 4b: Add the existing county to the list of counties.
                county_options.append(county_name)

                # 4c: Begin tracking the county's vote count.
                county_votes[county_name] = 0

            # 5: Add a vote to that county's vote count
            county_votes[county_name] += 1    

            candidate_name = row[2]  

            #if the candidate does not match any existing candidate..
            if candidate_name not in candidate_options:
                #Add it to the list of candidates
                candidate_options.append(candidate_name)

                #2 Begin tracking that candidate's vote count
                candidate_votes[candidate_name] = 0
                #print("** New Candidate ", candidate_name)

            #Add a vote to that candidate's count
            candidate_votes[candidate_name] +=1

        # Print the final vote count (to terminal)
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n")
        print(election_results, end="")

        txt_file.write(election_results)

        # 6a: Write a for loop to get the county from the county dictionary.     
        for county_name in county_votes:

            # Retrieve vote count and percentage
            votes = county_votes.get(county_name)
                
            # 6c: Calculate the percentage of votes for the county.       
            vote_percentage = float(votes) / float(total_votes) * 100
            county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # 6d: Print the county results to the terminal.
            print(county_results)
            
            #  6e: Save the county votes to a text file.
            txt_file.write(county_results)

            # 6f: Write an if statement to determine the winning county and get its vote count.
            if (votes > winning_county) and (vote_percentage > winning_percentage):
                winning_county = votes
                largest_county = county_name
                winning_percentage = vote_percentage

        # 7: Print the county with the largest turnout to the terminal.
        winning_county_summary = (
            f"-------------------------\n"
            f"Largest County Turnout: {largest_county}\n"
            f"-------------------------\n")
        print(winning_county_summary)

        # 8: Save the county with the largest turnout to a text file.
        txt_file.write(winning_county_summary)

        #Note: re-initialized because these variable are shared
        winning_count = 0
        winning_percentage = 0 

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

       

