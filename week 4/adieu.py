import inflect
import sys


p = inflect.engine()

names_list = []


while True:
    try:
        name = input("Name: ")
        names_list.append(name)
    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(names_list)}")
        break
