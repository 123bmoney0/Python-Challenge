#Dependencies
import os
import csv

#File Input & Output
csvpath = os.path.join('Desktop','PyPoll','Resources', 'election_data.csv')
csvpath_out = os.path.join('Desktop','PyPoll','Resources', 'election_data.csv')

#Variables
total_votes = 0
candidate_names = []
vote_count = []
    
#file Read    
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader, None)

#Loop to find candidates and votes    
    for row in csvreader:
        total_votes += 1
        if row[2] in candidate_names:
            vote_count[candidate_names.index(row[2])] += 1
        else:
            candidate_names.append(row[2])
            vote_count.append(1)
#Print
with open(csvpath_out, 'w', newline='') as text_file:

    text_file.write('Election Results' + '\n')
    text_file.write('-------------------------' + '\n')
    text_file.write('Total Votes: ' + str(total_votes) + '\n')
    text_file.write('-------------------------' + '\n')

    #Find vote count, vote percent & winner
    for i in range(len(candidate_names)):

        text_file.write(candidate_names[i] + ': ' + str(format(vote_count[i] / total_votes * 100, '.3f')) + '% (' + str(vote_count[i]) + ')\n')

    text_file.write('-------------------------' + '\n')
    text_file.write('Winner: ' + candidate_names[vote_count.index(max(vote_count))] + '\n')
    text_file.write('-------------------------')

with open(csvpath_out, newline='') as f:
    for line in f:
        print(line, end = '')
