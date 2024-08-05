import csv
import os

# specify relative file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# open file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    months = 0
    profit = 0
    start = 0
    lowChange = 0
    highChange = 0
    totalChange = 0

    # count months, find change in profit for each row and low and high change for whole table
    for row in csvreader:
        profit = profit + int(row[1])
        months += 1
        if start == 0:
            start = int(row[1])
        else:
            change = int(row[1]) - start
            start = int(row[1])
            totalChange = totalChange + change
            if change < lowChange:
                lowChange = change
                lowMonth = row[0]
            if change > highChange:
                highChange = change
                highMonth = row[0]

# find average change
avgChange = round(totalChange / (months - 1),2)
# cat output + print to terminal
output = 'Financial Analysis\n----------------------------\nTotal Months: ' + str(months) + '\nTotal: $' + str(profit) + '\nAverage Change: $' + str(avgChange) + '\nGreatest Increase in Profits: ' + highMonth + ' ($' + str(highChange) + ')\nGreatest Decrease in Profits: ' + lowMonth + ' ($' + str(lowChange) + ')'
print(output)
#open and write to new .txt file
newTextFile = open('financialAnalysis.txt', 'w')
newTextFile.write(output)
newTextFile.close()