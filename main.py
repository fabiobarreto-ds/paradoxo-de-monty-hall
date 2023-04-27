import random
lista1 = ["A", "B", "C"]
lista2 = ["A", "B"]
lista3 = ["A", "C"]
rodadas = 0
acertouComPrimeiraEscolha = 0
acertosDepoisQueMudou = 0
errouComSegundaEscolha = 0
errouComPrimeiraEscolha = 0
jogadas = int(input("Quantas jogadas você quer? Escolha números inteiros: "))
for c in range(0, jogadas):
    escolha = random.choice(lista1)
    print("=" * 50)
    print(f"Escolha uma das portas, A, B ou C?:")
    print(f"Você escolheu a {escolha}")
    rodadas += 1
    if escolha == "A":
        print(f"Irei abrir a porta B que não contém o prêmio, quer ainda continuar com a porta A ou mudar para a C?")
        escolha = random.choice(lista3)
        print(f"Na sua segunda chance você escolheu a {escolha}")
        if escolha == "A":
            print(f"Você continuou com a {escolha}, ACERTOU!!")
            acertouComPrimeiraEscolha += 1
            print("=" * 200)
        elif escolha == "C":
            print(f"Errou, você mudou para a {escolha}, a porta certa é a 'A'")
            errouComSegundaEscolha += 1
            print("=" * 200)
    elif escolha == "B":
        escolha = random.choice(lista2)
        print(f"Irei abrir a porta C que não contém o prêmio, quer ainda continuar com a porta B ou mudar para a A?")
        print(f"Na sua segunda chance você escolheu a {escolha}")
        if escolha == "A":
            print("Você acertou.")
            acertosDepoisQueMudou += 1
            print("=" * 200)
        elif escolha == "B":
            print("Você errou, a porta certa é a 'A'")
            errouComPrimeiraEscolha += 1
            print("=" * 200)
    elif escolha == "C":
        escolha = random.choice(lista3)
        print(f"Irei abrir a porta B que não contém o prêmio, quer ainda continuar com a porta C ou mudar para a A?")
        print(f"Na sua segunda chance você escolheu a {escolha}")
        if escolha == "A":
            print("Você acertou.")
            acertosDepoisQueMudou += 1
            print("=" * 200)
        elif escolha == "C":
            print("Você errou, a porta certa é a 'A'")
            errouComPrimeiraEscolha += 1
            print("=" * 200)
print(f"Número de rodadas = {rodadas}")
print(f"Acertos com o primeiro palpite: {acertouComPrimeiraEscolha}. Probabilidade de {(acertouComPrimeiraEscolha/jogadas)*100:.2f}% |||")
print(f"Errou com o primeiro palpite: {errouComPrimeiraEscolha}. Probabilidade de {(errouComPrimeiraEscolha/jogadas)*100:.2f}% |||")
print(f"Acertos com o segundo palpite: {acertosDepoisQueMudou}. Probabilidade de {(acertosDepoisQueMudou/jogadas)*100:.2f}% |||")
print(f"Errou com o segundo palpite: {errouComSegundaEscolha}. Probabilidade de {(errouComSegundaEscolha/jogadas)*100:.2f}%")
print(f"Tivesse mudado a porta no segundo palpite E acertou depois que mudou para o segundo palpite, a probabilidade de acerto seria de  {((acertosDepoisQueMudou/jogadas)*100 + (errouComPrimeiraEscolha/jogadas)*100):.2f}% |||")
print(f"Tivesse continuado com o primeiro palpite ou não tivesse mudado para o segundo palpite, a probabilidade de acerto seria de {((acertouComPrimeiraEscolha/jogadas)*100 + (errouComSegundaEscolha/jogadas)*100):.2f}% |||")
total = (acertouComPrimeiraEscolha/jogadas)*100 + (errouComPrimeiraEscolha/jogadas)*100 + (acertosDepoisQueMudou/jogadas)*100 + (errouComSegundaEscolha/jogadas)*100
print(f"TOTAL: {total}%")

