import os
import csv


dirname = os.path.dirname(__file__)
budgetcsvpath = os.path.join("Resources", "budget_data.csv")


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

#def financial_analysis(budget_data):

    #total_months = 0   
    #for row in csvreader:
     #   total_months += 1

    #net_total = 0
    #for row in csvreader:
   #     net_total += float(row[1])

  #  print(total_months)
 #   print(net_total)

#with open(budgetcsvpath) as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")
    #next(csvreader, None)

    #financial_analysis(csvreader)