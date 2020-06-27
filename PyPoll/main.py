# import libraries
import os
import csv

# set working directory to that of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# set path to the input file
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Initialize persistent variables (need these values across iterations of all rows)
votes = 0
candidates = {}

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header) (comment out print for final run)
    csv_header = next(csvreader)
    #print(csv_header)

    # Read each row of data after the header
    for row in csvreader:
        
        # For testing; comment this 'if' block out to run the whole input file
        #if votes == 50:
             #break

        # Also for testing; comment out for full run
        #print(row)

        # Give our row array values real names for this iteration of the loop
        voterId = row[0]
        county = row[1]
        candidate = row[2]
        
        # Iterate total vote count
        votes += 1
        
        # Iterate (or start) candidate-specific vote count
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
        
# from this point forward, the CSV file is no longer needed

# calculate results
results = []
winner = []

# iterate through the voted-for candidates
for candidate in candidates.items():
    
    # determine the current candidate's percentage of votes; round to 5 decimals (3 percent decimals)
    percentWon = round(candidate[1] / votes, 5)

    # stash the current candidate's results in a tuple (since we need 3 values)
    result = (candidate[0], percentWon, candidate[1])
    
    # stash the result tuple in a list
    results.append(result)

    # test to see if the current candidate got more votes than the current leader
    if len(winner) > 0:

        # if winner/leader is not yet populated, assume the first candidate is the leader and store their results
        if percentWon > winner[1]:
            winner[0] = candidate[0]
            winner[1] = percentWon
    
    else:

        # otherwise overwrite the winning result if the current candidate outperformed the current leader
        winner = [candidate[0], percentWon]

# print results to terminal
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {str(votes)}")
print("--------------------------------")

# iterate through the results to list out each voted-for candidate's result
for result in results:

    # format the vote percentage to show as a percent with 3 decimal places
    pct = "{:.3%}".format(float(result[1]))
    print(f"{result[0]}: {pct} ({str(result[2])})")

# output the remaining information to the terminal screen
print("--------------------------------")
print(f"Winner: {winner[0]}")
print("--------------------------------")
    
# output result to a Results.txt file in the project's Analysis folder
txtpath = os.path.join(".", "Analysis", "Results.txt")

# open a text file at the path specified; w = write-only, text, and overwrite if exists
with open(txtpath, "w") as txtfile:

    # output the results to the text file
    txtfile.write("Election Results\n")
    txtfile.write("--------------------------------\n")
    txtfile.write(f"Total Votes: {str(votes)}\n")
    txtfile.write("--------------------------------\n")

    # iterate through the results to list out each voted-for candidate's result
    for result in results:

        # format the vote percentage to show as a percent with 3 decimal places
        pct = "{:.3%}".format(float(result[1]))
        txtfile.write(f"{result[0]}: {pct} ({str(result[2])})\n")

    # output the remaining information to the text file
    txtfile.write("--------------------------------\n")
    txtfile.write(f"Winner: {winner[0]}\n")
    txtfile.write("--------------------------------\n")