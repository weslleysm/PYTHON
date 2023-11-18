# peça cinco nomes e coloque os nomes em uma lista
# Se o nome iniciar com Consoante avise "Seu nome inicia com Consoante"
# adicone um nome no inicio da lista e imprima a lista

nome1 = input("Digite o nome: ")
nome2 = input("Digite o nome: ")
nome3 = input("Digite o nome: ")
nome4 = input("Digite o nome: ")
nome5 = input("Digite o nome: ")

print(80 * '_')

lista = []
lista = [nome1, nome2, nome3, nome4, nome5]

if nome1[0] != 'a' and nome1[0] != 'e' and nome1[0] != 'i' and nome1[0] != 'o' and nome1[0] != 'u':
    print(nome1, 'Seu nome inicia com Consoante')

if nome2[0] != 'a' and nome2[0] != 'e' and nome2[0] != 'i' and nome2[0] != 'o' and nome2[0] != 'u':
    print(nome2, 'Seu nome inicia com Consoante')

if nome3[0] != 'a' and nome3[0] != 'e' and nome3[0] != 'i' and nome3[0] != 'o' and nome3[0] != 'u':
    print(nome3, 'Seu nome inicia com Consoante')

if nome4[0] != 'a' and nome4[0] != 'e' and nome4[0] != 'i' and nome4[0] != 'o' and nome4[0] != 'u':
    print(nome4, 'Seu nome inicia com Consoante')

if nome5[0] != 'a' and nome5[0] != 'e' and nome5[0] != 'i' and nome5[0] != 'o' and nome5[0] != 'u':
    print(nome5, 'Seu nome inicia com Consoante')

lista.insert (0, 'weslley')
print(lista, type(lista))