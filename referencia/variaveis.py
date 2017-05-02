#NUMEROS

# tres tipos : int, float e complex
# 1 = int, 1.0 = float, 1+2j = complex

numero_int = 10
numero_float = 5.5
numero_complex = 1+2j

print(numero_int, numero_float, numero_complex)

#Algumas operacoes

print(3 + 4.2) #retorna um float
print(4 / 2) #retorna float
print(5 / 2) #retorna float (divisao em ponto flutuante)
print(5 // 2) #retorna inteiro (divisao descartando parte fracionaria)
print(10 % 3) #retorna o resto (1)
print(2 ** 8) #potencia


#STRINGS

#strings = sequencia
estadio = "maracana"

print(estadio[0]) #retorna m
print(estadio[0:4]) #retorna mara
print(estadio[2:]) #retorna racana

#Algumas operacoes
string = "palavra"

print("m" in "maracana") #verifica se 'm' existe em 'maracana', retorna true
print("a" * 3) #retorna aaa
print(string.capitalize()) #retorna 'Palavra'
print(string.count("a")) #verifica quanta incidencias da letra 'a' contem em 'palavra', retorna 3
print(string.startswith("m")) #true
print(string.endswith("z")) #false
string = "varias palavra e mais palavras"
print(string.split(" ")) #retorna uma lista, ['varias', 'palavra', 'e', 'mais', 'palavras']
print(string.replace("a", "X")) #substitui as letras 'a' por 'X'


#INTERPOLACAO DE STRING

print("%d dias para copa" % (100)) #retorna '100 dias para copa'
print("{} dias para copa".format(100)) #retorna '100 dias para copa'
print("{dias} dias para copa".format( dias = 100 ) ) #mesma coisa

