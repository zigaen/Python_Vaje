import random

secret = random.randint(1,30)
attempts = 0


def cast_previous_score():
    with open("score.txt", "r") as score:
        last_score = int(score.read())
        print("Last score is:  " + str(last_score))
        return last_score


def write_score(new_score, past_score):
    if new_score < past_score:
        with open("score.txt", "w") as score_file:
            score_file.write(str(attempts))


def print_high_score(new_score, past_score):
    if new_score < past_score:
        print("     * New High score is : " +str(new_score))
    else:
        print("     * High score is : " +str(past_score))


def write_scores(new_score):
    with open("all_scores.txt", "r") as scores:
        last_scores = scores.read()
    new_score = f"{last_scores}, {new_score}"
    with open("all_scores.txt", "w") as scores:
        scores.write(str(new_score))
    print(f"       **** All scores are : {new_score}")



while True:

    attempts += 1
    guess = int(input("Guess the secret number (1-30): "))

    if guess == secret:
        print("You've guessed it! The number is: " + str(secret))
        print("     !Attempts needed: " + str(attempts))
        prev_score = cast_previous_score()
        write_score(attempts, prev_score)
        print_high_score(attempts, prev_score)
        write_scores(attempts)
        break

    if guess < secret:
        print("Try something bigger! " )
        print("   Attempt number: " + str(attempts + 1))
    elif guess > secret:
        print("Try something smaller!" )
        print("   Attempt number: " + str(attempts + 1))