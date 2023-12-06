# faça um programa que leia nome e media de um aluno, guardando também a situação em um dicionario. no final, 
# mostre o conteudo da estrutura na tela
dicionario = {}
nome = str(input('Informe seu nome:'))
media = float(input(f'{nome} informe sua media:'))

if media <= 6:
    situacao = 'Reprovado'
    print(f'o aluno {nome} foi Reprovado com media final:{media}')
    dicionario = {'nome':nome, 'media':media, 'situação':situacao,}
elif media > 6:
    situacao = 'Aprovado'
    print(f'o aluno {nome} foi Aprovado com a media:{media}')
    dicionario = {'nome':nome, 'media':media, 'situação':situacao,}
print(dicionario)
