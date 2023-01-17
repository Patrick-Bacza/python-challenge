# import os and csv in order to read in csv file
import os
import csv

# Read in csv 

csvpath = os.path.join('PyPoll' , 'Resources' , 'election_data.csv')

with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')


    
#Grab Headers

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# Create 'votes' list to house 'candidate' column. This is how we wil count the votes
# Create a variable for each candidate and set it equal to zero. This is how will store the count for each candidate
    votes = []
    stockham = 0
    degette = 0
    doane = 0

# Append 'votes' list with the 'candidate' column from the csv 
# To get the total votes, take the length of the votes list. 
# Store it in a variable called total_votes


    for row in csvreader:
        votes.append(row[2])
        total_votes = len(votes)

# Get vote count for each candidate
#       Use if statement. loop through the candidates column. Update each variable by one depending on whose name appears in the row
        
        if row[2] == 'Charles Casper Stockham':
            stockham = stockham + 1
        elif row[2] == 'Diana DeGette':
            degette = degette + 1
        else:    
            doane = doane + 1

# Calculate percentages 
#       Create three variables to house each candidates percentage of the vote 
#       Set variables equal to their votes divided by the total amount of votes and multiply by 100
#       Round decimal to three places

        s_percentage = round((stockham / total_votes) * 100 , 3)
        de_percentage = round((degette / total_votes) * 100 , 3)
        do_percentage = round((doane / total_votes) * 100 , 3)

# Create empty variable to house the winner

        winner = ''

# use if statement to set the winner variable to the candidate with the most votes

        if degette > stockham & doane:
            winner = 'Diana Degette'
        elif stockham > degette & doane:
            winner = 'Charles Casper Stockham'
        else:
            winner = 'Raymon Anthony Doane'

 # Use f strings to create print statments           


    print('Election Results')

    print('-----------------------')

    print(f'Total Votes: {total_votes}')

    print('-----------------------')

    print( f'Charles Casper Stockham:  {s_percentage}% ({stockham})' )

    print( f'Diana Degette:  {de_percentage}% ({degette})' )

    print( f'Raymon Anthony Doane:  {do_percentage}% ({doane})' )

    print('-----------------------')

    print(f'Winner: {winner}')

    print('-----------------------')

# Create list called 'lines' to house each f string

lines = ['Election Results' , '', '------------------------' ,'' , f'Total Votes: {total_votes}' , '' , '------------------------' , '' , f'Charles Casper Stockham:  {s_percentage}% ({stockham})',
         '' , f'Diana Degette:  {de_percentage}% ({degette})' , '' , f'Raymon Anthony Doane:  {do_percentage}% ({doane})' , '' , '-----------------------' , '' , f'Winner: {winner}',
         '' , '-----------------------' ] 

# Write the f strings to a text file using the 'lines' list

with open('Election_Results.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')








   
