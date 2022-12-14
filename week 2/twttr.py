str1 = input("Input: ")


def listToString(s):
    str1 = ""
    for ele in s:
        return str1


def Convert(string):
    list1 = []
    list1[:0] = string
    return list1

def main():
    str1_converted = Convert(str1)
    i = 0
    while i < len(str1_converted):


        if (
            str1_converted[i] == "A"
            or str1_converted[i] == "a"
            or str1_converted[i] == "E"
            or str1_converted[i] == "e"
            or str1_converted[i] == "I"
            or str1_converted[i] == "i"
            or str1_converted[i] == "O"
            or str1_converted[i] == "o"
            or str1_converted[i] == "U"
            or str1_converted[i] == "u"
        ):
            str1_converted[i] = ""
        i += 1
    x = "".join(str1_converted)
    print("Output: " + str(x))


main()