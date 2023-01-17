
import os
import csv

csvpath = os.path.join('PyPoll' , 'Resources' , 'election_data.csv')

with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
#Grab Headers

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    votes = []
    stockham = 0
    degette = 0
    doane = 0

    for row in csvreader:
        votes.append(row[2])
        total_votes = len(votes)
        
        if row[2] == 'Charles Casper Stockham':
            stockham = stockham + 1
        elif row[2] == 'Diana DeGette':
            degette = degette + 1
        else:    
            doane = doane + 1

        s_percentage = round((stockham / total_votes) * 100 , 3)
        de_percentage = round((degette / total_votes) * 100 , 3)
        do_percentage = round((doane / total_votes) * 100 , 3)

        winner = ''

        if degette > stockham & doane:
            winner = 'Diana Degette'
        elif stockham > degette & doane:
            winner = 'Charles Casper Stockham'
        else:
            winner = 'Raymon Anthony Doane'


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

lines = ['Election Results' , '', '------------------------' ,'' , f'Total Votes: {total_votes}' , '' , '------------------------' , '' , f'Charles Casper Stockham:  {s_percentage}% ({stockham})',
         '' , f'Diana Degette:  {de_percentage}% ({degette})' , '' , f'Raymon Anthony Doane:  {do_percentage}% ({doane})' , '' , '-----------------------' , '' , f'Winner: {winner}',
         '' , '-----------------------' ] 

with open('Election_Results.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')








   
