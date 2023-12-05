"""
Questão 01

• Escreva um programa que, recebe uma palavra, crie uma função que verifica na lista "alfabeto" a que indice pertence cada letra da palavra. Imprima os resultados.

Obs: você deve validar se a palavra tem três ou mais letras
Obs: letras repetidas devem ser verificadas somente uma vez

Exemplos do resultado:
    palavra = "cidade" 
    C está no indice 2
    I está no indice 8
    D está no indice 3
    A está no indice 0
    E está no indice 4
"""

#alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z' ]
def letras_indice(palavra, alfabeto):
    if len(palavra) < 3:
        print("A palavra tem que ter 3 ou mais letras.")
        
#a função index () é a maneira mais fácil de encontrar a posição de um elemento em uma lista Python
    for letra in set(palavra):
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            print(f"'{letra}' está no índice {indice} .")


alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

palavra = input("Digite uma palavra de no mínimo 3 letras: ").lower()

letras_indice(palavra, alfabeto)