#import modules
import os
import csv

#set path for file
dirname = os.path.dirname(__file__)
electioncsvpath = os.path.join("Resources", "Election_data.csv")

#declare variables
candidates = {}
total_votes = 0
max_votes = 0
winner = ""

#open csv and skip header
with open(electioncsvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   next(csvreader, None)

#sum total votes and find candidates that received votes
   for row in csvreader:
       total_votes = total_votes + 1
       if row[2] not in candidates:
           candidates[row[2]] = 1
       else:
           candidates[row[2]] = candidates [row[2]] + 1
# print("Election Results")  
# print("-----------------------------")        
# print(f"Total Votes: {total_votes}")
# print("-----------------------------")
# max_votes = 0
# winner = ""
def candidate_votes(Election_data):
    max_votes = 0
    winner = ""
    for name,votes in candidates.items():
        print(f"{name}: {100*votes/total_votes:.3f}% ({votes})")
        if votes > max_votes:
            winner = name
            max_votes = votes

print("Election Results")  
print("-----------------------------")        
print(f"Total Votes: {total_votes}")
print("-----------------------------")
candidate_votes(row)
print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")




