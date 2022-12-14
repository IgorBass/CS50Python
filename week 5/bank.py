def main():
    greeting = input("Greting: ")
    output = value(greeting)
    print(f'${output}')


def value(x):
    x = x.casefold().replace(" ","")
    if 'hello' in x:
        return 0
    elif x[0] == 'h' and x != 'hello':
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()

