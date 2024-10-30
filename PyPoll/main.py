# -*- coding: UTF-8 -*-
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1


# Calculate vote percentages and determine the winner
results = []

for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {vote_percentage:.3f}% ({votes})") # To 3 decimal points like in example output
    if votes > winning_count:
        winning_candidate = candidate
        winning_count = votes

# Generate the output summary
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    + "\n".join(results) +
    f"\n-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"-------------------------\n"
)

# Print the output to the terminal
print(output)

# Write the output to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
