# The data we need to retrieve
import csv
import os

#  Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

## Initialize Variables/List/Dictionaries 

#1) The total number of votes cast
total_votes = 0
#2) A complete list of candidated who recived votes
candidate_options = []
#3/4) Candiate Votes
candidate_votes = {}
#5) The winner of the election based on popular vote
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#A) Open the election results and read the file
with open(file_to_load) as election_data:
    
    # Read the file (reader function)
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)

     # FOR LOOP to get each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get candidate name from each row.
        candidate_name = row[2]

        # IF STATEMENT - Add Candidate and start traking
        if candidate_name not in candidate_options:
            #Add candidate
            candidate_options.append(candidate_name)
            # Create candidate as key as set candidate vote count to zero
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#B) Save the results to txt
with open(file_to_save, "w") as txt_file: 

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to txt.
    txt_file.write(election_results)

    # The % of votes each candidate won (by looping through the counts)
    #  Iterate through the candidate list to get candidate name
    for candidate_name in candidate_votes:
        # total number of votes each candidate won 
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            
        # print votes to the terminal.
        print(candidate_results)
        # save the candidate results to our text file.
        txt_file.write(candidate_results) 

        # The winner of the election based on popular vote
        # Determine winning vote count, % and candidate 
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes
            winning_count = votes
            #3. Set winning_percent = vote_percentage.
            winning_percentage = vote_percentage
            #4. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    #print winning candidates' results to the terminal. 
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)