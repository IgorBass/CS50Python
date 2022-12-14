import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    score = 0
    split_ip = re.split('\\.', ip)
    if len(split_ip) == 4:
        for number in split_ip:
            if int(number) in range(0,256):
                score += 1
            else:
                continue
        if score == 4:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
