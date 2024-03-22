import random


def boas_vindas():
    print("*********************************")
    print("Bem-vindo ao Jogo de Adivinhação")
    print("*********************************")


def obter_numero_secreto():
    return random.randint(1, 100)


def obter_nivel_dificuldade():
    while True:
        nivel = input("Qual o nível de dificuldade? (1) Fácil (2) Médio (3) Difícil: ")
        if nivel.isdigit() and int(nivel) in [1, 2, 3]:
            return int(nivel)
        else:
            print("Por favor, digite apenas os números 1, 2 ou 3.")


def obter_total_tentativas(nivel):
    return 20 if nivel == 1 else 10 if nivel == 2 else 5


def obter_chute():
    while True:
        chute = input("Digite o seu número: ")
        if chute.isdigit():
            return int(chute)
        else:
            print("Por favor, digite apenas números.")


def calcular_pontuacao(pontos, numero_secreto, chute):
    return max(pontos - abs(numero_secreto - chute), 0)


def jogar_jogo():
    boas_vindas()
    numero_secreto = obter_numero_secreto()
    nivel = obter_nivel_dificuldade()
    total_de_tentativas = obter_total_tentativas(nivel)
    pontos = 100

    for rodada in range(1, total_de_tentativas + 1):
        print("\nTentativa {} de {} ".format(rodada, total_de_tentativas))
        chute = obter_chute()

        if chute == numero_secreto:
            print("Você acertou!")
            break
        elif chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100.")
            continue
        elif chute > numero_secreto:
            print("Você errou! Seu chute foi maior do que o número secreto.")
        else:
            print("Você errou! Seu chute foi menor do que o número secreto.")

        pontos = calcular_pontuacao(pontos, numero_secreto, chute)
        print("Sua pontuação atual é:", pontos)

    print("\nFim do jogo")
    print("O número secreto era:", numero_secreto)
    print("Sua pontuação final é:", pontos)


if __name__ == "__main__":
    jogar_jogo()
