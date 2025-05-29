import random

game_running = True
player = {"name": "Tidus", "attack": 10, "turbo": 25, "heal": 16, "health": 100, "mana": 20}

print("---"*7)
print("Enter player name")
player["name"] = input()
    

while game_running:
    player["health"] = 100
    monster = {"name": "Monster", "attack": 12, "super": 20, "heal": 6, "health": 100}

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
        print("3) Exit game")

        player_choice = input("Your choice: ").strip()

        if player_choice == '1':
            # Player attacks
            crit = random.randint(1,10)
            if crit == "10":
                monster["health"]-= player["attack"]*2
                print(f"It's a citical hit! Monster health: {str(monster['health'])}")
                
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
                num = random.randint(1, 6)
                # print(f"Monster rolls: {num}")
                if num == 6:
                    monster["health"] += monster["heal"]
                    print(f"Monster heals! {str(monster['health'])}")
                else:
                    num2 = random.randint(1, 10)
                    # print(num2)
                    if num2 == 10:
                        player["health"] -= monster["super"]
                        print(f"Monster attacks you with a super attack! Your health: {str(player['health'])}")

                    else:
                        player["health"] -= monster["attack"]
                        print(f"Monster attacks you! Your health: {str(player['health'])}")
            else:
                player["health"] -= monster["attack"]
                print(f"Monster attacks you! Your health: {str(player['health'])}")

            if player["health"] <= 0:
                print("You were defeated!")
                monster_won = True
                new_round = False
                continue

        elif player_choice == '2':
            # Player heals
            player["health"] = min(player["health"] + player["heal"], 100)
            print(f"You healed! Your health: {str(player['health'])}")

            # Monster turn
            if monster["health"] < 95:
                num = random.randint(1, 6)
                # print(f"Monster rolls: {num}")
                if num == 6:
                    monster["health"] += monster["heal"]
                    print("Monster heals!")
                else:
                    player["health"] -= monster["attack"]
                    print(f"Monster attacks you! Your health: {str(player['health'])}")
            else:
                player["health"] -= monster["attack"]
                print(f"Monster attacks you! Your health: {str(player['health'])}")

            if player["health"] <= 0:
                monster_won = True
                print("You were defeated!")
                new_round = False
                continue


        elif player_choice == "3":
            new_round = False
            game_running = False
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

   
        


