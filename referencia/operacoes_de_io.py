#Operações de IO

#cria arquivo (nome_arquivo, modo_de_operacao)
# w = modo escrita (re-escreve arquivo), a = escreve arquivo e permite concatenar conteudo
# r = modo de leitura

arquivo = open("../arquivo.txt", "w").close() #modo escrita

arquivo = open("../arquivo.txt", "a") #modo append(permite inserir conteudo)
arquivo.write("banana\n")
arquivo.write("melancia\n")
arquivo.write("abacaxi\n")
arquivo.write("laranja\n")
arquivo.close()

arquivo = open("../arquivo.txt", "r") #modo leitura(nao permite inserir conteudo)
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
arquivo = open("../arquivo.txt", "r")
conteudo = arquivo.readline()
print(conteudo)
arquivo.close()

#Além do r, w e a existe o modificador b que devemos utilizar quando queremos trabalhar no modo binário.
#Para abrir uma imagem devemos usar:
#arquivo copia.py
#logo = open('python-logo.png', 'rb')
#data = logo.read()
#logo.close()

#logo2 = open('python-logo2.png', 'wb')
#logo2.write(data)
#logo2.close()