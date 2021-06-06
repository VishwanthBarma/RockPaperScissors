import random


def menu():
    print("Select any of the options mentioned below : ")
    print("0 - Quit Game")
    print("1 - Play Game")


def play(output_list):
    print("Game Started : ")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissor")
    while True:
        try:
            choice = int(input("Choose any option from above to play (0 - quit) : "))
        except ValueError:
            print("-------Entered Invalid Syntax-------")
            continue
        choices_list = [1, 2, 3]
        if choice == 0:
            break
        if choice not in choices_list:
            print("-------Entered Invalid Syntax-------")
            continue

        print("You Selected - ", output_list[choice])
        ran_int = random.randint(1, 3)
        # 1 - Rock, 2 - Paper, 3 - Scissor
        print("Computer Selected - ", output_list[ran_int])
        if choice == ran_int:
            print("************Game Tied************")
            continue
        elif (choice == 1 and ran_int == 2) or (choice == 2 and ran_int == 3) or (choice == 3 and ran_int == 1):
            print("************Computer Won************")
            continue
        elif (choice == 1 and ran_int == 3) or (choice == 2 and ran_int == 1) or (choice == 3 and ran_int == 2):
            print("************You Won************")
            continue
        else:
            print("-----Entered Invalid Syntax-----")
            continue


print("*************Rock-Paper-Scissors**************")

outputs = {1: "Rock", 2: "Paper", 3: "Scissor"}
quit_game = False

while not quit_game:
    menu()
    click = int(input("Select Option : "))
    options = [0, 1]
    if click not in options:
        print("Entered Invalid Syntax")
        continue
    if click == 0:
        print("Quiting the Game")
        quit_game = True
        continue
    if click == 1:
        play(outputs)
        continue

print("Game Ended Successfully, Thank you for visiting.")
