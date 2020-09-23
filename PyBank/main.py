import os
import csv

# Set path for file
dirname = os.path.dirname(__file__)
budgetcsvpath = os.path.join("Resources", "budget_data.csv")


# Open the CSV
with open(budgetcsvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    total_months = 0   
    for row in csvreader:
        total_months += 1
    
    print(total_months) 

with open(budgetcsvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    total = 0
    for row in csvreader:
        total += float(row[1])

    print(total)