# Import os and csv 

import os
import csv 

 
month_year = []
profit_loss = []


# Write in csv file

csvpath = os.path.join('PyBank' , 'Resources' , 'budget_data.csv')

with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
#Grab Headers

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
# Loop through file, append profit loss list with values changed to integers and run calculations

    for row in csvreader:
        month_year.append(row[0])
        profit_loss.append(int(row[1]))
        total_months = len(profit_loss)
        total = sum(profit_loss)
        max_increase = max(profit_loss)
        max_decrease = min(profit_loss)
        max_increase_date = month_year[profit_loss.index(max_increase)]
        max_decrease_date = month_year[profit_loss.index(max_decrease)]



   


print('Financial Analysis')

print('------------------------')

print(f'Total Months: {total_months}')

print(f'Total: ${total}')

print(f'Greatest Increase in Profits: {max_increase_date} ({max_increase})')

print(f'Greatest Decrease in Profits: {max_decrease_date} ({max_decrease})')


    
        




