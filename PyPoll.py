# The data we need to retrieve
import csv
import os

#  Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. The total number of votes cast

# a) Initialize a total vote counter.
total_votes = 0

#2. A complete list of candidated who recived votes
candidate_options = []

#2a. The % of votes each candidate won 

# a) Declare the empty dictionary.
candidate_votes = {}

#5. The winner of the election based on popular vote
# Winning Candidate and Winning Count Tracker 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# b) Open the election results and read the file
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

     # 1. Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # 2. candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#3. The % of votes each candidate won (by looping through the counts)

    # 1. Iterate through the candidate list.
for candidate_name in candidate_votes:

    #4. the total number of votes each candidate won 

    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # print votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #5. The winner of the election based on popular vote
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

  