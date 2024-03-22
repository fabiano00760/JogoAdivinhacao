




print("*********************************")
print("Bem-vindo ao Jogo de Adivinhação")
print("*********************************")

numero_secreto = 42


def obter_chute():
    while True:
        chute = input("Digite o seu número: ")
        if chute.isdigit():
            return int(chute)
        else:
            print("Por favor, digite apenas números.")


while True:
    chute = obter_chute()
    print("Você digitou o número:", chute)

    if chute == numero_secreto:
        print("Você acertou!")
        break
    elif chute > numero_secreto:
        print("Você errou! Seu chute foi maior do que o número secreto.")

    else:
        print("Você errou! Seu chute foi menor do que o número secreto.")

print("Fim do jogo")
