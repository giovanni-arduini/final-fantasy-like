import random

game_running = True
player = {"name": "Tidus", 
          "attack": 10, 
          "turbo": 25, 
          "heal": 16, 
          "health": 100, 
          "speed": 10, 
          "mana": 2, 
          "turbo_bar": 0}

print("---"*7)
print("Enter player name")
player["name"] = input()
    

while game_running:
    player["health"] = 100
    player["mana"] = 2
    player["turbo_bar"] = 0

    monster = {"name": "Monster", 
               "attack": 12, 
               "super": 20, 
               "heal": 6, 
               "health": 100, 
               "speed": 8}

    print("---"*7)
    print("New round... Fight!")

    print(player["name"] + " has " + str(player["health"])+ " health.")
    print(monster["name"] + " has " + str(monster["health"])+ " health.")
    new_round = True

    print("---"*7)


    while new_round == True:

        player_won = False
        monster_won = False

        print("Select action")
        print("1) Attack")
        print("2) Heal")
        if player["turbo_bar"] >= 20:
            print("3) Turbo Attack")
        print("0) Exit game")
        print("Mana: " + str(player["mana"]))

        player_choice = input("Your choice: ").strip()

# Player attack
        if player_choice == '1':
            # Player turn
            crit = random.randint(1,10)
            monster_dodge = random.randint(1, 100) + monster["speed"] - player["speed"]

            if crit == "10":
                monster["health"]-= player["attack"]*2
                print(f"It's a citical hit! Monster health: {str(monster['health'])}")

            if monster_dodge > 93:
                print("The monster dodged your attack!")    

            else:
                monster["health"] -= player["attack"]
                print(f"You attack the monster! Monster health: {str(monster['health'])}")

            if monster["health"] <= 0:
                print("You defeated the monster!")
                player_won = True
                new_round = False
                continue

            # Monster turn
            if monster["health"] < 95:
                # monster heals
                monster_heal = random.randint(1, 6)
                dodge = random.randint(1, 100) + player["speed"] - monster["speed"]
                if monster_heal == 6:
                    monster["health"] += monster["heal"]
                    print(f"Monster heals! {str(monster['health'])}")
                elif dodge > 90:
                    print("You dodged the attack!")
                else:
                     # monster super
                    monster_super = random.randint(1, 10)
                   
                    if monster_super == 10:
                        player["health"] -= monster["super"]
                        player["turbo_bar"] += random.randint(1,3)
                        player["turbo_bar"] = min(player["turbo_bar"],20)
                        print(f"Monster attacks you with a super attack! Your health: {str(player['health'])}")
    

                    else:
                         # monster attack
                        player["health"] -= monster["attack"]
                        player["turbo_bar"] += random.randint(1,2)
                        player["turbo_bar"] = min(player["turbo_bar"],20)

                        print(f"Monster attacks you! Your health: {str(player['health'])}")
            else:
                player["health"] -= monster["attack"]
                player["turbo_bar"] += random.randint(1,2)
                player["turbo_bar"] = min(player["turbo_bar"],20)
                print(f"Monster attacks you! Your health: {str(player['health'])}")

            if player["health"] <= 0:
                print("You were defeated!")
                monster_won = True
                new_round = False
                continue

# Player heals
        elif player_choice == '2':
            # Player turn
            if player["mana"] <= 0:
                print("You don't have enough mana!")
                continue
            else:
                player["health"] = min(player["health"] + player["heal"], 100)
                print(f"You healed! Your health: {str(player['health'])}")
                player["mana"] = max(player["mana"]-2, 0)

            # Monster turn
            if monster["health"] < 95:
                num = random.randint(1, 6)
                dodge = random.randint(1, 100) + player["speed"]
                if num == 6:
                    monster["health"] += monster["heal"]
                    print("Monster heals!")
                elif dodge > 90:
                    print("You dodged the attack!")
                else:
                    player["health"] -= monster["attack"]
                    player["turbo_bar"] += random.randint(1,3)
                    player["turbo_bar"] = min(player["turbo_bar"],20)
                    print(f"Monster attacks you! Your health: {str(player['health'])}")
            else:
                player["health"] -= monster["attack"]
                player["turbo_bar"] += random.randint(1,2)
                player["turbo_bar"] = min(player["turbo_bar"],20)
                print(f"Monster attacks you! Your health: {str(player['health'])}")

            if player["health"] <= 0:
                monster_won = True
                print("You were defeated!")
                new_round = False
                continue

# Turbo attack
        elif player["turbo_bar"] >= 20 and player_choice == "3":
            monster["health"] -= player["turbo"]
            print("You hit the monster with a TURBO attack!")

        elif player_choice == "0":
            new_round = False
            game_running = False
        else:
            print("Invalid choice. Please enter one of the commands above.")

        print("Turbo charge: " + str(player["turbo_bar"]))
   
        


