try:

    while True:
        number = input('Number: ')
        x = number.split('/')

        first_number = x.pop(0)
        first_number = int(first_number)

        second_number = x.pop()
        second_number = int(second_number)
        if first_number <= second_number:
            break


    fuel = round(((first_number / second_number) * 100) , 0)
    fuel = int(fuel)

    if fuel < 2:
        print('E')
    elif fuel > 98:
        print('F')
    else:
        print(f'{fuel}%')
except ValueError:
    number = input("Number: ")
except ZeroDivisionError:
    number = input("Number: ")