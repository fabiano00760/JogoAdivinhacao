import random

print("*********************************")
print("Bem-vindo ao Jogo de Adivinhação")
print("*********************************")

numero_secreto = random.randrange(0, 100)
print(numero_secreto)

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

while True:
    nivel = input("Defina seu nível: ")

    if nivel.isdigit():
        nivel = int(nivel)

        if nivel in [1, 2, 3]:
            break
        else:
            print("Por favor, digite apenas os números 1, 2 ou 3.")
    else:
        print("Por favor, digite apenas números.")

if nivel == 1:
    totalDeTentativas = 20
elif nivel == 2:
    totalDeTentativas = 10
else:
    totalDeTentativas = 5


def obter_chute():
    while True:
        chute = input("Digite o seu número: ")
        if chute.isdigit():
            return int(chute)
        else:
            print("Por favor, digite apenas números.")


for rodada in range(1, totalDeTentativas + 1):
    print("Tentativa {} de {} ".format(rodada, totalDeTentativas))
    chute = obter_chute()
    print("Você digitou ", chute)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100.")
        continue

    if chute == numero_secreto:
        print("Você acertou!")
        break
    elif chute > numero_secreto:
        print("Você errou! Seu chute foi maior do que o número secreto.")
    else:
        print("Você errou! Seu chute foi menor do que o número secreto.")

print("Fim do jogo")
print("O número secreto é: " + str(numero_secreto))
