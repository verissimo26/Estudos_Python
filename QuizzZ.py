print("Welcome to my QuIzZZ")

playng = input("Do you wanna play? ").lower()

score = 0

if playng == "sim":
    print("ok vamos jogar")

else:
    print("ok volte em breve")

answer = input("what does the CPU means to you ")
if answer.lower() == "central processing unit":
    print("corret")
    score = score + 1
else:
    print("incorret")

answer = input("what does the RAM means to you ")
if answer.lower() == "Virtual memory":
    print("corret")
    score = score + 1
else:
    print("incorret")

answer = input("what does the GPU means to you ")
if answer.lower() == "grafics processor":
    print("corret")
    score = score + 1
else:
    print("incorret")

answer = input("lula is a thief? ")
if answer.lower() == "sim":
    print("corret")
    score = score + 1
else:
    print("incorret")

if score == 1 or 0:
    print("Você acertou só " + str(score) + " Questão")
else:
    print("Você acertou " + str(score) + " Questões")

print("Sua média de acerto foi " + str((score / 4) / 100) + " % ")
if score < 3:
    print("não desanime continue estudando")
else:
    print("você está no caminho certo")
