import re
import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    x = s.find('0')
    first_two_letetrs = s[0:2]
    char_berfore_zero = x - 1
    sum_check = 1

    if 2 <= len(s) <= 6:
        sum_check = sum_check + 1
    else: return False

    if first_two_letetrs.isalpha():
        sum_check = sum_check + 1
    else: return False

    if s.isalnum():
        sum_check += 1
    else: return False

    if x != -1:
        if s[char_berfore_zero].isnumeric():
            sum_check = sum_check + 1
        else: return False

    if s[-3].isnumeric() and s[-2].isalpha():
        return False
    elif s[-2].isnumeric():
        sum_check = sum_check + 1



    if s.isalpha():
        sum_check = sum_check + 1
    elif s[-1].isalpha():
        return False

    if sum_check >= 4:
        return True
    else:
        return False


main()