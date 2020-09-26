#import modules
import os
import csv

#set path for file
dirname = os.path.dirname(__file__)
budgetcsvpath = os.path.join("Resources", "budget_data.csv")

#declare variables
total_months = 0
net_total = 0
profit_loss = []
months = []
change = []

#open csv
with open(budgetcsvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   next(csvreader, None)  

#sum total months and net total, add to months and profit loss list   
   for row in csvreader:
       total_months += 1
       net_total += int(row[1])
       profit_loss.append(int(row[1]))
       months.append(row[0])

#create list of change in profit/loss
   for i in range(1,len(profit_loss)):
        change.append((int(profit_loss[i]) - int(profit_loss[i - 1])))

#calculate average change
   average_change = sum(change) / len(change)

#calculate greatest increase and decrease
greatest_increase = max(change)
greatest_decrease = min(change)

#print information
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: {round(average_change,2)}")
print(f"Greatest Increase in Profits: {months[change.index(max(change))+1]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {months[change.index(min(change))+1]} (${(str(greatest_decrease))})")

#choose location of and open output file
output_file = os.path.join("Analysis", "Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    
#write to output file 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {total_months}")
    file.write("\n")
    file.write(f"Total: ${net_total}")
    file.write("\n")
    file.write(f"Average Change: {round(average_change,2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {months[change.index(max(change))+1]} (${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {months[change.index(min(change))+1]} (${(str(greatest_decrease))})")
