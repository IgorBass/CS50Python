price = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
#input oreder from user
total = 0
while True:
    try:
        order = input("Item: ")
        order = order.title()
        total = price[order] + total
        print(f"Total: ${total:.2f}")
    except EOFError:
        break
    except KeyError:
        print()





