import datetime
import random
import json  #vrsta zapisa, ki ga bere tudi java itd. Jason prebere zapise, ki jih python ne more interpretirati pravilno

pl_name = input("Napiši svoje ime:")
#definition of variables
wrong_attempt = []
secret = random.randint(1, 30)
attempts = 0
current_time = datetime.datetime.now()


#write to object
class ObjectScore:
    def __init__(self, attempts, player_name, date, secret):
        self.attempts = attempts
        self.player_name = player_name
        self.date = date
        self.secret = secret

    def to_dict(self):
        return self.__dict__

#Preberemo datoteko score_list.txt
with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Previous Scores: ")
with open("score.txt", "r") as score_f:
    score_l = json.loads(score_f.read())

#izpis prdhodnjega rezultata
score_list = sorted(score_list, key=lambda k: k["attempts"])[:3]
for score_dict in score_list:
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}".format(score_dict.get("player_name"),
                                                                                                                     str(score_dict.get("attempts")),
                                                                                                                     score_dict.get("date"),
                                                                                                                     score_dict.get("secret_number"),
                                                                                                                     score_dict.get("wrong"))
    print(score_text)


while True:
    #write gues in variable
    attempts += 1
    guess = random.randint(1, 30)
    print("Guess the secret number (1-30): ")
    #write if succesful guess
    if guess == secret:
        #write to dictionary
        score_list.append({"attempts": attempts, "date": str(current_time), "player_name": pl_name, "secret_number": secret, "wrong": wrong_attempt})
        #excercise - write to object
        object = ObjectScore(
            attempts=attempts,
            player_name=pl_name,
            date=str(current_time),
            secret=secret
        )
        score_l.append(object.to_dict())
        print(type(score_l))
        print(score_l)
        with open("score.txt", "w") as object_file:
            object_file.write(json.dumps(score_l, indent=1))
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list, indent=2))

        print("You've guessed it! The number is: " + str(secret))
        print("     !Attempts needed: " + str(attempts))
        break

    if guess < secret:
        print("Try something bigger! " )
        print("   Attempt number: " + str(attempts + 1))
        wrong_attempt.append(guess)


    elif guess > secret:
        print("Try something smaller!" )
        print("   Attempt number: " + str(attempts + 1))
        wrong_attempt.append(guess)


