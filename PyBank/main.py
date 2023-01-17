# Import os and csv 

import os
import csv 

month_year = []
profit_loss = []




csvpath = os.path.join('PyBank' , 'Resources' , 'budget_data.csv')

with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        profit_loss.append(int(row[1]))
        total_months = len(profit_loss)
        total = sum(profit_loss)
        max_increase = max(profit_loss)
        max_decrease = min(profit_loss)
    if row[1] == str(max_increase):
        max_month = row[0]


print('Financial Analysis')

print('------------------------')

print(f'Total Months: {total_months}')

print(f'Total: ${total}')

print(f'Greatest Increase in Profits: {max_month} ({max_increase})')

print(f'Greatest Decrease in Profits: {min_month} ({max_decrease})')


    
        




