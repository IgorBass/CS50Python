greeting = input("Greting: ")

greeting = greeting.casefold()

greeting = greeting.replace(" ","")

print(greeting)

if 'hello' in greeting:
    print('$0')
elif greeting[0] == 'h' and greeting != 'hello':
    print('$20')
else:
    print('$100')
