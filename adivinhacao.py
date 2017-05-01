import random

print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3

print(numero_secreto)

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um numero de 1 a 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um numero de 1 a 100")
        continue

    acertou = (chute == numero_secreto)
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    # Condicional em Python
    if(acertou):
        print("Você acertou!") #obrigatório identação com 4 espacos(tab)
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o numero secreto.")
        elif(menor): #equivalente a elseif em java
            print("Você errou! O seu chute foi menor que o numero secreto.")



print("Fim do Jogo")