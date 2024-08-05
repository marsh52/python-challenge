import csv
import os
# establish path to csv
csvpath = os.path.join('Resources', 'election_data.csv')

# create array to hold candidate information + vote counter
candidates = []
votes = 0

# open file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header
    csv_header = next(csvreader)
    # count votes, add candidates to array 
    for row in csvreader:
        votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
    # add vote counts to array for each candidate
    for i in range(len(candidates)):
        csvfile.seek(0)
        individualVotes = 0
        for row in csvreader:
            if row[2] == candidates[i]:
                individualVotes += 1
        candidates[i] = [candidates[i], individualVotes]

winnerVal = 0
# calculate percentage for each candidate
for i in range(len(candidates)):
    perc = 0
    candidateVotes = int(candidates[i][1])
    candidateName = candidates[i][0]
    perc = round(((candidateVotes)/votes) * 100, 3)
    candidates[i] = [candidateName, candidateVotes, perc]
    # declare winner
    if candidateVotes > winnerVal:
        winnerVal = candidateVotes
        winnerName = candidateName

line = '-------------------------\n'
# cat output
output1 = 'Election Results\n' + line + 'Total Votes: ' + str(votes) + '\n' + line
output2 = line + 'Winner: ' + winnerName + '\n' + line
# print output to terminal
print(output1, end = '')
for candidate in candidates:
    print(f'{candidate[0]}: {candidate[2]}% ({candidate[1]})')
print(output2, end = '') 
# write output to .txt file
newTextFile = open('election_results.txt', 'w')
newTextFile.write(output1)
for candidate in candidates:
    newTextFile.write(f'{candidate[0]}: {candidate[2]}% ({candidate[1]})\n')
newTextFile.write(output2)
newTextFile.close()