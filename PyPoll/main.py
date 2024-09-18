# File paths
file_path = 'Resources/election_data.csv'
output_file_path = 'analysis/election_results.txt'

# Initialize variables to store election data
total_votes = 0
candidate_votes = {}

# Read the CSV file
with open(file_path, 'r') as f:
    next(f)  # Skip the header
    
    for line in f:
        # Split the line by commas
        _, _, candidate = line.strip().split(',')
        
        # Increment the total vote count
        total_votes += 1
        
        # Count votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate vote percentages and determine the winner
winner = None
max_votes = 0
results = []

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))
    
    # Determine the winner by comparing votes
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Sort the results by vote count in descending order
results.sort(key=lambda x: x[1], reverse=True)

# Prepare the output
output = [
    "Election Results",
    "----------------------------",
    f"Total Votes: {total_votes}",
    "----------------------------"
]

for candidate, votes, percentage in results:
    output.append(f"{candidate}: {percentage:.2f}% ({votes})")

output.append("----------------------------")
output.append(f"Winner: {winner}")
output.append("----------------------------")

# Write results to the output file
with open(output_file_path, 'w') as f:
    for line in output:
        f.write(line + '\n')

# Display the final output
print("\n".join(output))
