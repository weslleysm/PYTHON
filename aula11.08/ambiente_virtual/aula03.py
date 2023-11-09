#Operadores IN e NOT IN (DENTRO e NÃO DENTRO)
nome = "Weslley"
print( 'es' in nome) #Pergunta: python, o "es" está contido na variavel "nome"

nao_nome = "joãzinho"
print ("au" not in nao_nome) # a função NOT vai da um valor falso para uma variavel verdadeiro

print('='*20)

seu_nome = input('Informe seu nome: ')
buscar = input('Informe o valor a ser encontrado: ')

if (buscar in seu_nome):
    print(f'{buscar} está contido em {seu_nome}')
else:
    print(f'{buscar} NÃO está contido em {seu_nome}')
