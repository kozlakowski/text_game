import time

# TUTAJ ZACZYNAM OPISYWAĆ/TWORZYĆ FUNKCJE UŻYWANE PÓŹNIEJ W GRZE !!!!!!!!!!!!!!!!!!!!!!!!
def starting_position():
    return (" YOUR POSITION\nRight now you're on the 'Rynek Główny', it's your starting position, it's a place full of people\n"
    "You can only go right or left(you see everything from the air perspective:D)\n"
    "Decide where you want to go, remember you have to find 'Stary Rudzielec', he is somewhere in the city\n")




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











elif "no" in first_decision:
    for i in range(5):
        print("Just close this game and don't waste your time kid!!")
        time.sleep(1)
