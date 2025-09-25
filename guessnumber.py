import random

number = random.randint(1, 20)
guess = int(input("Guess a number between 1 and 20: "))

if guess == number:
    print("Correct! You guessed it.")
else:
    print("Wrong! The number was", number)
