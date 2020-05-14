import json

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

answer_game = input("Add player forr football(f) or. basketball (b)? : ")
if answer_game == "b":
    while True:
        answer = input("Let's add a player to the list. Would you like to do that? (y/n): ")
        answer = answer.lower()
        if answer == "n":
            print("Ok, bye!")
        elif answer == "y":
            myPlayer = BasketballPlayer(
                first_name= input("Type first name of the player: "),
                last_name= input("Type last name of the player: "),
                height_cm= input("Player height: "),
                weight_kg= input("Player weight: "),
                points= input("The number of points: "),
                rebounds= input("The number of rebounds: "),
                assists= input("The number of assists: ")
            )
            print(f"{myPlayer.first_name} {myPlayer.last_name}   Will be stored in to database!")
            myPlayer = myPlayer.__dict__

            with open("player_list_basketball.txt", "r") as player_file:
                player_list = json.loads(player_file.read())
                print("Added player is: " + str(myPlayer))
                player_list.append(myPlayer)
            with open("player_list_basketball.txt", "w") as player_file:
                    player_file.write(json.dumps(player_list))
            continue

        else:
            print("enter the rigt letter (y/n)")
        break
elif answer_game == "f":
    while True:
        answer = input("Let's add a player to the list. Would you like to do that? (y/n): ")
        answer = answer.lower()
        if answer == "n":
            print("Ok, bye!")
        elif answer == "y":
            myPlayer = FootballPlayer(
                first_name=input("Type first name of the player: "),
                last_name=input("Type last name of the player: "),
                height_cm=input("Player height: "),
                weight_kg=input("Player weight: "),
                goals=input("The number of goals: "),
                yellow_cards=input("The number of yellow cards: "),
                red_cards=input("The number of red cards: ")
            )
            print(f"{myPlayer.first_name} {myPlayer.last_name}   Will be stored in to database!")
            myPlayer = myPlayer.__dict__

            with open("player_list_football.txt", "r") as player_file:
                player_list = json.loads(player_file.read())
                print("Added player is: " + str(myPlayer))
                player_list.append(myPlayer)
            with open("player_list_football.txt", "w") as player_file:
                player_file.write(json.dumps(player_list))
            continue

        else:
            print("enter the rigt letter (y/n)")
        break
else:
    print("You must choose between b/f! ")



