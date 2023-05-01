import random

user_wins = 0
computer_wins = 0

options = ["Pedra", "Papel", "Tezoura"]

while True:
    user_input = input("Type : Pedra,Papel,Tezoura ou Q to Quit \n").lower
    if user_input == "q":
        break

    if user_input in options:
        continue

    random_number = random.randint(0,2)

    computer_choice = options [random_number]
    print("CPU Choice: ", computer_choice + ".")

    if user_input == "rock" and computer_choice == "tezoura":
        print ("you won")
        user_wins += 1
    elif user_input == "paper" and computer_choice == "pedra":
        print("you won")
        user_wins += 1
    elif user_input == "tezoura" and computer_choice == "paper":
        print("you won")
        user_wins += 1
    else:
        print("you lost")
        computer_wins += 1
        continue



