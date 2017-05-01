import forca
import adivinhacao

print("********************************")
print("********ESCOLHA SEU JOGO!*******")
print("********************************")

print("(1) Forca  (2) Adivinhação")

jogo = int(input("Escolha o jogo: "))

if(jogo == 1):
    print()
    forca.jogar()
elif(jogo == 2):
    print()
    adivinhacao.jogar()