# import libraries
import os
import csv

# set working directory to that of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# set path to the input file
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Initialize persistent variables (need these values across iterations of all rows)
months = 0
prevPnlAmount = 0
maxIncrease = ["", 0]
maxDecrease = ["", 0]
pnlSum = 0
changeSum = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(csv_header)

    # Read each row of data after the header
    for row in csvreader:
        
        # For testing; comment this 'if' block out to run the whole input file
        #if months == 50:
        #     break

        # Also for testing; comment out for full run
        #print(row)

        # Give our row array values real names for this iteration of the loop
        month = row[0]
        pnlAmount = int(row[1])
        
        # Iterate month count and Profit/Loss sum
        months += 1
        pnlSum += pnlAmount
        
        # Do not do change analysis on the first month; we don't know what its change actually is
        if months > 1:
            
            #change is the difference between the current amount and the previous amount (stored in the previous iteration of the loop)
            change = pnlAmount - prevPnlAmount
            
            # add the change to the running change sum that will ultimately be used to get the average change
            changeSum += change

            # test for max increase
            if change > maxIncrease[1]:
                
                # store both month and amount if a higher increase is found
                maxIncrease = [month, change]

            # test for max decrease
            if change < maxDecrease[1]:

                # store both month and amount if a higher increase is found
                maxDecrease = [month, change]

        # set current amount to be the previous amount before advancing to the next row
        prevPnlAmount = pnlAmount

# from this point forward, the CSV file is no longer needed

# average change is the calculated change sum divided by the count of months
avgChange = round(changeSum / (months - 1), 2)

# prototype printing (for testing; comment out for full run)
#print("Financial Analysis")
#print("--------------------------------")
#print(f"Total Months: {str(months)}")
#print(f"Total: ${str(pnlSum)}")
#print(f"Average Change: ${str(avgChange)}")
#print(f"Greatest Increase in Profits: {maxIncrease[0]} (${str(maxIncrease[1])})")
#print(f"Greatest Decrease in Profits: {maxDecrease[0]} (${str(maxDecrease[1])})")

# output result to a Results.txt file in the project's Analysis folder
txtpath = os.path.join(".", "Analysis", "Results.txt")

# open a text file at the path specified; w = write-only, text, and overwrite if exists
with open(txtpath, "w") as txtfile:

    # output the results to the text file
    txtfile.write("Financial Analysis\n")
    txtfile.write("--------------------------------\n")
    txtfile.write(f"Total Months: {str(months)}\n")
    txtfile.write(f"Total: ${str(pnlSum)}\n")
    txtfile.write(f"Average Change: ${str(avgChange)}\n")
    txtfile.write(f"Greatest Increase in Profits: {maxIncrease[0]} (${str(maxIncrease[1])})\n")
    txtfile.write(f"Greatest Decrease in Profits: {maxDecrease[0]} (${str(maxDecrease[1])})\n")