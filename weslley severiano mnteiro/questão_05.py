"""
Questão 05

• Escreva um programa que atenda as requisições abaixo e imprima todos os resultados:

01. monte um conjunto(SET) com o nome "meu_conjunto1", nele você deve colocar os indices impares da "minha_lista"
02. transforme a "minha_lista" em uma string separada por /
03. monte uma lista iversa da "minha_lista"                                                               CONCLUIDA
04. informe quanntos elementos estão contidos em "minha_lista" e quantos estão contidos em "meu_conjunto" CONCLUIDO 
OBS: nao fiz a quantidade de elemetos que estão em "meu_conjuto", pois ele é feito na 01.

"""


minha_lista = ["com", "um", "notebook", "e", "internet", "de", "banda", "larga", "qualquer", "jovem", "capacitado", "poderá", "trabalhar", "ou", "empreender", "do", "Ceará", "para", "o", "Brasil", "e", "o", "mundo", "e", "consequentemente", "transformando", "a", "sua", "vida", "e", "aquecendo", "a", "economia", "local"]

meu_conjunto1 = set(minha_lista[0::1]) #01
print(meu_conjunto1)                   #"set" tranforma a lista em um sequencia desordenada e com os elementos únicos(não repetidos)

separador = '/'                        #2
string = separador.join(minha_lista)   # "join "Utilizados para transformar uma lista em uma string
print(string)                          #  concatenar elementos e utilizando um separador especificado

lista_inversa = minha_lista[::-1]   #03
print(lista_inversa)

contidos = len(minha_lista)
print(f'estão contidos {contidos} elementos na lista ')  #04
