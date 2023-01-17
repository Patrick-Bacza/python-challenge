# Import os and csv 

import os
import csv 

# Create lists to house columns from csv 
date = []
profit_loss = []


# Write in csv file

csvpath = os.path.join('PyBank' , 'Resources' , 'budget_data.csv')

with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

    
#Grab Headers

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
# Loop through file, append lists with the respective columns and calculate total months and net total

    for row in csvreader:
        date.append(row[0])
        profit_loss.append(int(row[1]))
        total_months = len(profit_loss)
        total = sum(profit_loss)

# Create Average period change / Greatest Increase / Greatest Decrease
#   1. Remove the first date from the date list as this does not have a prior period to compare it too   

    date.remove(date[0])

#   2. Copy the profit_loss list twice to period 1 and period 2 to create the period changes
 
    period_1 = profit_loss.copy()
    period_1.remove(period_1[0])

#  3. Remove the first value from period_1 and last value from period_2
#           This aligns each date with the prior date

    period_2 = profit_loss.copy()
    period_2.remove(period_2[85])

#   4. Create empty list to house the period changes
    period_changes = []

#   5. zip the two lists (period_1 and period_2) together and run a for loop on their values
#            1. append period_changes list with the difference of each item in order to get the period_changes
#            2. sum the period_chnages list and divide by its length to get teh average. Store it in Average_change variable
#            3. 
    for value1 , value2 in zip(period_1 , period_2):
        period_changes.append(value1 - value2)
        average_change = round(sum(period_changes) / len(period_changes),2)
        max_increase = max(period_changes)
        max_decrease = min(period_changes)
        max_increase_date = date[period_changes.index(max_increase)]
        max_decrease_date = date[period_changes.index(max_decrease)]


print('Financial Analysis')

print('------------------------')

print(f'Total Months: {total_months}')

print(f'Total: ${total}')

print(f'Average Change: ${average_change}')

print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})')

print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})')


lines = ['Financial Analysis' , '', '------------------------' ,'' , f'Total Months: {total_months}' , '' ,  f'Total: ${total}' , '' , f'Average Change: ${average_change}' ,
        '' , f'Greatest Increase in Profits: {max_increase_date} ({max_increase})' , '' , f'Greatest Decrease in Profits: {max_decrease_date} ({max_decrease})' ]  

with open('Financial_Analysis.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

        




