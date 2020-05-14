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

lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2, rebounds=7.4, assists=7.2)

kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)

ronaldo = FootballPlayer(first_name="Cristiano", last_name="Ronaldo", height_cm=184, weight_kg=79, goals=586, yellow_cards=95, red_cards=11)

messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)

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

    with open("player_list.txt", "r") as player_file:
        player_list = json.loads(player_file.read())
        print("Added player is: " + str(myPlayer))
        player_list.append(myPlayer)
    with open("player_list.txt", "w") as player_file:
            player_file.write(json.dumps(player_list))

else:
    print("enter the rigt letter (y/n)")



