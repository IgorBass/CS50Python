fruits =	{
  "apple": 130,
  "avocado": 50,
  "banana": 110,
  "cantaloupe": 50,
  "grapefruit": 60,
  "grapes": 90,
  "melon": 50,
  "kiwifruit": 90,
  "lemon": 15,
  "lime": 20,
  "nectarine": 60,
  "orange": 80,
  "peach": 60,
  "pear": 100,
  "pineapple": 50,
  "plums": 70,
  "strawberries": 50,
  "sweetcherries": 100,
  "tangerine": 50,
  "watermelon": 80,
}

item = input("Item: ")
y = item.casefold().strip().replace(' ', '')
if y in fruits:
    x = fruits.get(y)
    print("Calories: "+str(x))
else:
    print('')
