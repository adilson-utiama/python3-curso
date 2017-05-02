#LISTAS

#Alguns exemplos de declaracoes de lista
#listas sao MUTAVEIS, podem ser alteradas e manipuladas a qualquer momento

numeros = [1,2,3,4,5]
palavras = ["salario", "imposto"]
misto = [1, 2, 3, "palavra", "outra_palavra"]
misto2 = [1, 2, 3, ["palavra", "frase"], "salario", numeros] #armazena de tudo

#algumas operacoes
print(misto2[3][1]) #retorna  'frase'
print(misto2[5][0:2]) #retorna 1, 2
print("Total de itens {}".format(len(misto2))) #retorna o total de itens da lista
numeros.append(6) #adiciona elemento ao final da lista
numeros.insert(2, 10) #adiciona elemnto no indice indicado insert(indice, valor)
numeros.pop() #elimina ultimo elemento da lista
print(numeros)

#for valor in misto2:
 #   print(valor)

