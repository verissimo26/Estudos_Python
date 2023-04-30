import random

user_wins = 0
computer_wins = 0
def roll():
    return random.randrange(0,2)

option = ["Pedra", "Papel", "Tezoura"]

while True:
    user_input = input("Type: Pedra, Papel, Tezoura ou Sair  ").lower()
    if user_input == "sair":
        break

    if user_input not in option:
        print("escolha um valor valido")
        break

    computer_choice = option[roll()]
    print("CPU Choice ", computer_choice + ".")






