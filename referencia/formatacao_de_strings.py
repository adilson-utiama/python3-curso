#Interpolação de string e formatações

print("Tentativa {} de {}".format(1,3))
    #saida: Tentativa 1 de 3

print("Tentativa {1} de {0}".format(1,3))
    #saida: Tentativa 3 de 1

print("R$ {:f}".format(1.59)) # f de float
    #saida: R$ 1.590000

print("R$ {:07d}".format(4)) # d(digitos) se refere a valores de tipo int
    #saida: R$ 0000004

print("R$ {:.2f}".format(1.5)) # em :.2f define quantos caracteres vem depois de .
    #saida: R$ 1.50

print("R$ {:7.2f}".format(1234.50))
print("R$ {:7.2f}".format(1.5))
    #saida: R$ 1234.50
    #       R$    1.50

print("R$ {:07.2f}".format(1.5))
    #saida: R$ 0001.50

print("Data {:02d}/{:02d}".format(19, 11))
    #saida: Data 19/11