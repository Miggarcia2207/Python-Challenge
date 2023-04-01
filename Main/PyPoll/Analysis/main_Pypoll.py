#PyPoll
import csv

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

with open("election_data.csv") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        total_votes += 1
        
        if row[2] not in candidates:
            candidates[row[2]] = 0
        
        candidates[row[2]] += 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidates:
    votes = candidates[candidate]
    percent = votes / total_votes * 100
    print(f"{candidate}: {percent:.3f}% ({votes})")
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
