import random

while True:
    try:
        user_level = int(input("Level: "))
        random_number = random.randint(1, user_level)
        break
    except ValueError:
        ...

while True:
    try:
        user_guess = int(input("Guess: "))
        if user_guess < random_number:
            print("Too small!")
        elif user_guess > random_number:
            print("Too large!")
        elif user_guess == random_number:
            print("Just right!")
            break
    except ValueError:
        ...

