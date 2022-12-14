from collections import Counter
grocery = []
keys = []
counter ={}
i = 0
while True:
        try:
            order = input()
            order = order.upper()
            i += 1
            keys.append(i)
            grocery.append(order)
            grocery.sort()
            res = dict(zip(keys, grocery))
            values = res.values()
            counter = dict(Counter(values))
        except EOFError:
            for key in counter:
                print(counter.get(key), end=" " )
                print(key)
            break
