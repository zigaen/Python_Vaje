import random
secret = random.randint(1, 30)
guess = 0

while guess != secret:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess < secret:
        print("You misseed it - the number is BIGGER")
    elif guess > secret:
        print("You misseed it - the number is smaller")
    else:
        print("Correct, the number is:  " + str(guess))