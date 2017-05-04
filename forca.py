import random

def jogar():
    print("********************************")
    print("***Bem vindo ao jogo da Forca***")
    print("********************************")

    arquivo = open("arquivo.txt", "r")
    palavras = []
    for letra in arquivo:
        letra = letra.strip()
        palavras.append(letra)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta] #List Comprehension

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        print(letras_acertadas)
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

    if (acertou):
        print(letras_acertadas)
        print("Você ganhou!")
    else:
        print(letras_acertadas)
        print("Você perdeu!")

    print("Fim do Jogo")


if (__name__ == "__main__"):
    jogar()