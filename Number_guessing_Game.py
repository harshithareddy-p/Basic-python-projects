import random

num = random.randint(1, 100)

print("-----NUMBER GUESSING GAME-----")

while True:
    try:
        x = int(input("Enter your guess:"))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if 1 <= x <= 100:
        if num > x:
            print("Too low! Keep trying 😎")
        elif num < x:
            print("Too high!Keep trying 😎")
        else:
            print("Congoo, You've guessed it right!⭐")
            break
    else:
        print("Please enter a number ONLY between 1 and 100!")
