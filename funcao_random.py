import random

print(random.random()) #retorna um float de 0.0 ate 1.0

print(1 + random.random() * 100)  #retorna um float de 1.0 ate 100.0

numero_inteiro = int(1 + random.random() * 100)  #retorna um inteiro de 1 ate 100
print(numero_inteiro)

numero = (1 + random.random() * 100)
numero_arredondado = round(numero)  # a funcao round() arredonda um float
print(numero_arredondado) # imprime um inteiro


print(random.randrange(1, 101))  # imprime de 1 a 100