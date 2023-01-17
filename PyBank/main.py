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

    month_year.remove(month_year[0])

    
    period_1 = profit_loss.copy()
    period_1.remove(period_1[0])

    period_2 = profit_loss.copy()
    period_2.remove(period_2[85])

    period_changes = []

    for item1 , item2 in zip(period_1 , period_2):
        period_changes.append(item1 - item2)
        average_change = round(sum(period_changes) / len(period_changes),2)
        max_increase = max(period_changes)
        max_decrease = min(period_changes)
        max_increase_date = month_year[period_changes.index(max_increase)]
        max_decrease_date = month_year[period_changes.index(max_decrease)]


print('Financial Analysis')

print('------------------------')

print(f'Total Months: {total_months}')

print(f'Total: ${total}')

print(f'Average Change: ${average_change}')

print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})')

print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})')


lines = ['Financial Analysis' , '', '------------------------' ,'' , f'Total Months: {total_months}' , '' ,  f'Total: ${total}' , '' , f'Average Change: ${average_change}' ,
        '' , f'Greatest Increase in Profits: {max_increase_date} ({max_increase})' , '' , f'Greatest Decrease in Profits: {max_decrease_date} ({max_decrease})' ]  

with open('Analysis.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

        




