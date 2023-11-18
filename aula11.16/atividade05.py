# peça cinco nomes e coloque os nomes em uma lista
# Se o nome iniciar com Vogal avise "Seu nome inicia com vogal"
# remova o nome do meio
nome = input('Digite o nome: ')
nome2 = input('Digite o nome: ')
nome3 = input('Digite o nome: ')
nome4 = input('Digite o nome: ')
nome5 = input('Digite o nome: ')

nomes = []
nomes = [nome, nome2, nome3, nome4, nome5]

print(80 * '_')

if nome[0] == 'a' or nome[0] == 'e' or nome[0] == 'i' or nome[0] == 'o' or nome[0] == 'u':
    print(nome, 'Seu nome inicia com vogal')

if nome2[0] == 'a' or nome2[0] == 'e' or nome2[0] == 'i' or nome2[0] == 'o' or nome2[0] == 'u':
    print(nome2, 'Seu nome inicia com vogal')

if nome3[0] == 'a' or nome3[0] == 'e' or nome3[0] == 'i' or nome3[0] == 'o' or nome3[0] == 'u':
    print(nome3, 'Seu nome inicia com vogal')

if nome4[0] == 'a' or nome4[0] == 'e' or nome4[0] == 'i' or nome4[0] == 'o' or nome4[0] == 'u':
    print(nome4, 'Seu nome inicia com vogal')

if nome5[0] == 'a' or nome5[0] == 'e' or nome5[0] == 'i' or nome5[0] == 'o' or nome5[0] == 'u':
    print(nome5, 'Seu nome inicia com vogal')

del nomes [2]
print(nomes, type(nomes))