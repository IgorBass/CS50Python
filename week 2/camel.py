import re

name = input("camelCase: ")
name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
print("snake_case: " + name)