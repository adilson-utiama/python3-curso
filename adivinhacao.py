print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42

chute_str = input("Digite o numero: ")
print("Você digitou " , chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

# Condicional em Python
if(acertou):
    print("Você acertou!") #obrigatório identação com 4 espacos(tab)
else:
    if(maior):
        print("Você errou! O seu chute foi maior que o numero secreto.")
    elif(menor):
        print("Você errou! O seu chute foi menor que o numero secreto.")

print("Fim do Jogo")