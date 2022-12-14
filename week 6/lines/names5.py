with open("names.txt") as file:
    lines = file.readlines()
for line in lines:
    print("hello,", line.rstrip())
    print
# Reads from a file