#Pypoll

#Election Audit

##Overview of Project

For this week's Python challenge, we were instructed to generate a vote count report for a U.S congressional precinct in Colorado.  As part of the election audit, the report takes into account all the votes casted through the three primary voting methods: mail-in ballots, punch cards, and direct recording electronic counting machines.  The report is usually generated in Excel, but we would like to know if there's a way to automate the process using Python.  To do this, phyton code was written and executed to confirm the code was working.  After the code generated through the use of Phyton was submitted, additional data was requested to finalize the audit.  This written report provides a brief overview of the process.
 
### *Purpose* 

The purpose of this project was to generate a vote count report in Python for the election audit.


##Election_Audit Results

Data was provided to us in the form of a comma-separated value (CSV) file with each value being separated by a comma.  Both Python code and text files were created using this data.     
  

### *Election Results Printed to the Command Line*

Based on the data, and as seen in Figure 1, there was a total of 369,712 votes casted in this congressional election.

Figure 1

![election_results_terminal ](https://user-images.githubusercontent.com/115508896/205478230-1ccc56fb-ee31-4dd2-ade1-d04df44ba4e4.png)

Figure 1 is a screen shot of the code's output printed on the terminal and it shows the breakdown of the number of votes and the percentage of total votes for each county in the precinct.  This precinct had three counties known as Jefferson, Denver, and Arapahoe.  As an example, Jefferson county had 38,855 votes which is 10.5% of the total votes.  Furthermore, with 306,055 votes, Denver was the county with the largest number of votes.   


### *Election Results Saved to a Text File*

The Python script also created a new text file and Figure 2 shows the screenshot of such text file.

Figure 2

![election _results_txt](https://user-images.githubusercontent.com/115508896/205478258-8f0191ea-92f6-476e-8454-d06efcf55476.png)

Based on the results in Figure 2, there were three candidates within this preceint with Diana DeGette as the election winner.  Diana DeGette won with 272,892 votes and a 73.8% of the total votes. 

##Election-Audit Summary
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
