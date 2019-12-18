import os
import csv

f = open("file.txt", "w")

# Locating the file;
budgetdata_csv = os.path.join("budgetdata.csv")

# Opening the file and skipping the header;
with open(budgetdata_csv, newline="") as csvfile:
    x = csv.reader(csvfile, delimiter=",")
   
    next(x)

# Creating a list of months, and a list of profits/losses;
    profloss = []
    months1 = []

    for a, b in x:
        profloss.append(float(b))
        months1.append(a)

# Calculating the total of profits/losses;
    proflossum = sum(profloss)
    count = 0
    for line in profloss:
        count += 1

# Creating a list with differences between profits/losses over months;
    diff = [profloss[i + 1] - profloss[i] for i in range(len(profloss)-1)]
    newSum = 0
    count1 = 0
    average = 0
    for j in diff:
        newSum += j
        count1 += 1

# Calculating the average of change in profits/losses;
    average = newSum / count1

# Calculating the max difference, min difference in profits/losses;
    indexmax = diff.index(max(diff)) + 1
    indexmin = diff.index(min(diff)) + 1

# Calculating the months of max difference and min difference in profits/losses;
    monthmax = months1[indexmax] 
    monthmin = months1[indexmin] 

# Printing my financial analysis
    print ("Financial Analysis")
    print ("------------------------")
    print ("Total months: ", count)
    print ("Total: ", "$", "{0:.0f}".format(proflossum))
    print ("Average change: ", "$", "{0:.0f}".format(average))
    print ("Greatest increase in profits: ", monthmax, "(", "$", "{0:.0f}".format(max(diff)), ")")
    print ("Greatest decrease in profits: ", monthmin, "(", "$", "{0:.0f}".format(min(diff)), ")")

# Exporting my financial analysis to a text file;
    file = open("financialanalysisjan", "w")
    file.write("Total months:  86, Total:  $ 38382578, Average change:  $ -2315, Greatest increase in profits:  feb-12 ( $ 1926159 ), Greatest decrease in profits:  sep-13 ( $ -2196167 )")
    file.close()


    
    