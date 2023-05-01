# import random
#
# top_of_range = input("Type a number: ")
#
# if top_of_range.isdigit():
#     top_of_range = int(top_of_range)
#
#     if top_of_range <= 0:
#         print('Please type a number larger than 0 next time.')
#         quit()
# else:
#     print('Please type a number next time.')
#     quit()
#
# random_number = random.randint(0, top_of_range)
# guesses = 0
#
# while True:
#     guesses += 1
#     user_guess = input("Make a guess: ")
#     if user_guess.isdigit():
#         user_guess = int(user_guess)
#     else:
#         print('Please type a number next time.')
#         continue
#
#     if user_guess == random_number:
#         print("You got it!")
#         break
#     elif user_guess > random_number:
#         print("You were above the number!")
#     else:
#         print("You were below the number!")
#
# print("You got it in", guesses, "guesses")
#
# # ______________________ DADO VIRTUAL ESTÁ DANDO ERRO ____________________________

# import random

# def roll():
#     return random.randrange(0,7)
#
# rolar_os_dados = "sim"
#
# input("gostaria de rolar os dados? \n")
#
# while rolar_os_dados == True:
#     print(roll())
#     input("gostaria de rolar os dados de novo? \n")
#     quit()

# ______________________ DADO VIRTUAL MELHORADO ____________________________
import random
def roll():
    return random.randrange(0,7)

resultado =[]

rolar_os_dados = input("Gostaria de rolar os dados? \n").lower()
if rolar_os_dados == "sim":
    rolar_os_dados = roll()
    print(roll())
   
else:
    print("Ok volte em breve")
    quit()

# rolar_os_dados2 = input("Gostaria de rolar os dados? 2º tentativa \n").lower()
# if rolar_os_dados2 == "sim":
#
#     print(roll())
# else:
#     print("Ok volte em breve")
#     quit()
#
# rolar_os_dados3 = input("Gostaria de rolar os dados? 2º tentativa \n").lower()
# if rolar_os_dados3 == "sim":
#     print(roll())
# else:
#     print("Ok volte em breve")
#     quit()

print("obrigado por jogar")






