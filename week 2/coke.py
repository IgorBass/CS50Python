amount_due = 50
insert_coin = 0
need_coin = [25, 10, 5]

while True:
    amount_due = amount_due - insert_coin
    if amount_due <= 0:
        change_owed = 0 - amount_due
        print("Change Owed: " + str(change_owed))
        break
    while True:
        print("Amount Due " + str(amount_due))
        insert_coin = int(input('Insert Coin: '))
        if insert_coin in need_coin:
            break
