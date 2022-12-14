from tabulate import tabulate
import sys
import csv

listoflist = []
try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith("csv") == False:
        sys.exit("Not a CSV file")
    elif len(sys.argv) == 2:
        with open(sys.argv[1], "r") as file:
            for line in file:
                row = line.rstrip().split(",")
                listoflist.append(row)
        print(tabulate(listoflist, headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
