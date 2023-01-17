# Import os and csv in order to read in the csv file

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
        net_total = sum(profit_loss)

# Create Average period change / Greatest Increase / Greatest Decrease
#   1. Copy the date list and remove the first date from the date list as this does not have a prior period to compare it too   
    date_2 = date.copy()
    date_2.remove(date[0])

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
#            2. sum the period_changes list and divide it by its length to get the average change. Store it in Average_change variable
#            3. use max() and min() to get the max increase and max decrease. Store them in the max_increase and max_decrease variables respectively
#            4. The index for the values found in period_changes will match up with the values in the date list
#                   Use index() to find the index for the max_increase and max_decrease values
#                   Use those indexes to grab the values from the date list 
#                   Add them to the max_increase_date abd max_decrease_date variables respectively

    for value1 , value2 in zip(period_1 , period_2):
        period_changes.append(value1 - value2)
        average_change = round(sum(period_changes) / len(period_changes),2)
        max_increase = max(period_changes)
        max_decrease = min(period_changes)
        max_increase_date = date_2[period_changes.index(max_increase)]
        max_decrease_date = date_2[period_changes.index(max_decrease)]

# Create print statements useing f strings and the variables created above

print('Financial Analysis')

print('------------------------')

print(f'Total Months: {total_months}')

print(f'Total: ${net_total}')

print(f'Average Change: ${average_change}')

print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})')

print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})')

#  Add fstrings to list called lines

lines = ['Financial Analysis' , '', '------------------------' ,'' , f'Total Months: {total_months}' , '' ,  f'Total: ${net_total}' , '' , f'Average Change: ${average_change}' ,
        '' , f'Greatest Increase in Profits: {max_increase_date} ({max_increase})' , '' , f'Greatest Decrease in Profits: {max_decrease_date} ({max_decrease})' ]  

# Write the f strings to a text file using the 'lines' list
with open('Financial_Analysis.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

        




