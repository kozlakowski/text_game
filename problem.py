import time

# TUTAJ ZACZYNAM OPISYWAĆ/TWORZYĆ FUNKCJE UŻYWANE PÓŹNIEJ W GRZE !!!!!!!!!!!!!!!!!!!!!!!!

def starting_position():
    return (" YOUR POSITION\nRight now you're on the 'Rynek Główny', it's your starting position, it's a place full of people\n"
    "You can only go right or left(you see everything from the air perspective:D)\n"
    "Decide where do you want to go, remember you have to find 'Stary Rudzielec', he is somewhere in the city\n")

def right_left_move():
    global right_left
    right_left = input("Go right or left? : ")
    if right_left == "right":
        return "So you've moved right!\n"
    elif right_left == "left":
        return "So you've moved left!\n"
    else:
        return "You should enter yes/no"

def tavern_position():
    return ("You're in the most famous town's place, it's Tavern.\n"
    "You can eat and drink here, but be careful, it's full of bad people\n")

def arsenal_position():
    return ("You're in mysterious place, it's an old arsenal. Usually nobody is here,\n"
    "but now you see a weird man standing in the corner. You should ask him about 'Stary Rudzielec'\n")

def drink_or_not():
    print("Now you have to decide.You can stay here, start drinking and have fun or you can\n"
    "leave this place and go back to the starting position('Rynek Główny') and complete your mission.\n")
    global drinking_hm
    drinking_hm = input("So what is you decision?(type stay/leave) : ")
    if drinking_hm == "stay":
        return "You've lost the game, your laziness and lack of discipline made you do that"
    elif drinking_hm == "leave":
        return "That's a good move, you are going back to the starting position('Rynek Główny')\n"

def try_another_way():
    return ("Now you are again in starting position. I recommend you to start a new game and fix your mistakes\n"
    "by choosing another ways.\n")

# TU ZACZYNA SIĘ KOD KONKRETNIE GRY, KOŃCZĄ SIĘ FUNKCJE
print("Hello There ...\n")
time.sleep(2)
print("Welcome to the 'Problem'\n")

while True:
    first_decision = input("Do you want to play? : ")

    if first_decision == "yes":
        print("So here your story begins...\n")
        break
    elif first_decision == "no":
        print("It's your decision, but you'll regret it.\n")
        break
    else:
        print("You have to decide. Type yes/no\n")

if "yes" in first_decision:
    # time.sleep(3)
    print("You're in dangerous place.\nIt's ancient Poland, many people live here, many agressive and unpredictable people.\n"
    "Your mission is to find an old guy named 'Stary Rudzielec' and ask him for help. He will know how to make Poland great again!\n")
    # time.sleep(3)
    print(starting_position())
    print(right_left_move())
    if right_left == "right":
        print(tavern_position())
        print(drink_or_not())
        if drinking_hm == "stay":
            exit()
        elif drinking_hm == "leave":
                print(starting_position())
                print(try_another_way())
    elif right_left == "left":
        print(arsenal_position())















elif "no" in first_decision:
    print("JUST CLOSE THIS GAME AND DON'T WASTE YOUR TIME KID!!")
    time.sleep(3)
    exit()
