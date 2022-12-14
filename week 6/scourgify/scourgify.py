import sys
import csv

try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith("csv") == False:
        sys.exit("Not a Python file")
    elif len(sys.argv) == 3:
        with open(sys.argv[1], "r") as csv_file:
            fields = ['name', 'house']
            dict, names, after =[], [], []
            csv_reader = csv.DictReader(csv_file, fieldnames=fields)
            for row in csv_reader:
                dict.append(row)
            for i in range(len(dict)-1):
                name = (dict[i+1]["name"].split(", "))
                after.append([name[1], name[0], dict[i+1]["house"]])
        with open(sys.argv[2], 'w', newline="") as new_file:
            fieldnames = ['first', 'last', 'house']
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            csv_writer.writerow({"first": "first", "last": "last", "house": "house"})
            for j in range(len(after)):
                csv_writer.writerow({"first": after[j][0], "last": after[j][1], "house": after[j][2]})


except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")
