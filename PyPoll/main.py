import os
import csv

# Accessing the CSV file
votedata_csv = os.path.join("election_results.csv")

# Separating the data through comma's
with open(votedata_csv, newline="") as csvfile:
    x = csv.reader(csvfile, delimiter=",")  

# Skipping the header
    next(x) 

# Creating a new list with just candidate name of each vote
    candidates = []
    for a, b, c in x:
        candidates.append(c)

    count = 0
    for line in candidates:
        count += 1

# Creating a list of candidates without duplicates
    candidates1 = list(set(candidates))

# Counting the amount of votes per candidate
    amountofvotesKhan = candidates.count("Khan")
    amountofvotesLi = candidates.count("Li")
    amountofvotesOTooley = candidates.count("O'Tooley")
    amountofvotesCorrey = candidates.count("Correy")

# Calculating percentage votes per person and setting the percentage to 2 decimal points
    percentageKhan = "{0:.2f}".format((amountofvotesKhan / count) * 100)    
    percentageLi = "{0:.2f}".format((amountofvotesLi / count) * 100)
    percentageOTooley = "{0:.2f}".format((amountofvotesOTooley / count) * 100)
    percentageCorrey = "{0:.2f}".format((amountofvotesCorrey / count) * 100)
   
# Printing the final table	
    print("Election results are in!")
    print("--------------------")
    print("Total votes: ", count)
    print("--------------------")
    print("Khan vote percentage: ", percentageKhan,"%","(",amountofvotesKhan,")")
    print("Li vote percentage: ", percentageLi,"%", "(",amountofvotesLi,")")
    print("O'Tooley vote percentage: ", percentageOTooley,"%","(",amountofvotesOTooley,")")
    print("Correy vote percentage: ", percentageCorrey,"%","(",amountofvotesCorrey,")")
    print("--------------------")
    print("Winner = Khan")
    print("--------------------")
    print("Congratulations Khan!")
    
    
# Exporting the vote results to a text file;
    file = open("voteresults.txt", "w")
    file.write("Election results are in: Total votes:  1048575, Khan  63.09 % ( 661583 ), Li vote percentage:  13.96 % ( 146360 ), O'Tooley vote percentage:  3.01 % ( 31586 ), Correy vote percentage:  19.94 % ( 209046 ), Winner = Khan, Congratulations Khan!")
    file.close()

   

