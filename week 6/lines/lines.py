import sys
import tabulate

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith("py") == False:
        sys.exit("Not a Python file")
    elif len(sys.argv) == 2:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
        row = 0
        for line in lines:
            x = line.strip()
            if x == '':
                row += 0
            elif x.startswith("#") or x.startswith("\n"):
                row += 0
            else:
                row += 1
        print(row)


except FileNotFoundError:
    sys.exit("File does not exist")
