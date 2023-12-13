# Escreva um código que, recebe três palavras e uma frase, crie uma função que verifique se as palavras aparecem
# COMPLETAS na frase e indique qual intervalo de índices ele foi encontrada. Você deve utilizar uma lista para 
# realizar a atividade.

# Obs.: você deve validar se a palavra tem três ou mais letras
# Obs.: você deve validar se a frase tem pelo menos 20 palavras

def linha_branco ():
    print()

frase = input('Informe uma frase:')

linha_branco()

print(frase)


while len (frase) < 10:
    frase = input('Digite uma frase maior:')
palavra1 = input('Digite uma palavra:')

linha_branco()

while len (palavra1) < 3:
    palavra1 = input('Digite uma paavra maior ou igual a 3 caracteres:')
print('Verificação da 1º palavra digitada:')

linha_branco()

cont = 0 
for i in frase:
    if i == palavra1:
        print(f'a palavra {i} aparece na frase no indice{cont}.')
    cont =+1

linha_branco()

palavra2 = input('Informe uma palavra:')

linha_branco()

print('VERIFICAÇÃO DA SEGUNDA PALAVRA.')

linha_branco()

while len (palavra2) < 2:
    palavra2 = input('Digite uma palavra com 3 ou mais caractere.')
cont2 = 0
for i in frase:
    if i == palavra2:
        print(f'A palavra {i} aparece na frase no indice {cont2}')
    cont2 += 1

