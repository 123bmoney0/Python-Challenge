import os
import csv

csvpath = os.path.join('Desktop','PyBank', 'Resources', 'budget_data.csv')
csvpath_out = os.path.join('Desktop','PyBank', 'Resources', 'budget_data.csv')

with open(csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader, None)

    total_months = 0
    total_income= 0
    change = []
    average_change = 0
    average = 0
    greatest_increase = 0
    greatest_decrease = 0
    prior = 0
    

    for row in csvreader:
        total_months += 1
        total_income += int(row[1])
        
        difference = int(row[1]) - int(prior)
        prior = row[1]
        change.append(difference)
        average = sum(change) / len(change)

        if int(row[1]) - average_change > greatest_increase:
            greatest_increase = int(row[1]) - average_change
            greatest_increase_month = row[0]
        elif int(row[1]) - average_change < greatest_decrease:
            greatest_decrease = int(row[1]) - average_change
            greatest_decrease_month = row[0]
          

        average_change = int(row[1])

with open(csvpath_out, 'w', newline= '') as text_file:

    text_file.write('Financial Analysis\n')
    text_file.write('----------------------------\n')
    text_file.write('Total Months: '+str(total_months) + '\n')
    text_file.write('Total: $'+str(total_income) + '\n')
    text_file.write('Average Change: '+str(average) + '\n')
    text_file.write('Greatest Increase in Profit: '+greatest_increase_month+' ($'+str(greatest_increase) + ')\n')
    text_file.write('Greatest Decrease in Profits:'+greatest_decrease_month+' ($'+str(greatest_decrease) + ')\n')

with open(csvpath_out, newline= '') as f:
    for line in f:
        print(line, end = '')