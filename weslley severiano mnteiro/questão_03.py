"""
Questão 03

• Escreva um programa que atenda as requisições abaixo e imprima todos os resultados:

01. imprima quantas veze aparece a letra "a" no "texto".   concluida
02. imprima qual a posição do primeiro "z".                concluida
03. leve o "texto" para uma nova variavel e trocando "aprendizado compartilhado" por "vivencia profissional".

"""
texto = "Somos uma escola de tecnologia de informação que cria pontes entre pessoas, conhecimento e empresas. Ambiente que proporciona conexão, troca de conhecimentos e aprendizado compartilhado entre participantes, instrutores e empresas parceiras."
quantidade = 0
for i in texto:           # 01
    if i in 'a':
        quantidade += 1
print(f'a letra "a" aparece {quantidade} vezes no texto')


letra = 'a'
print(texto.count(letra))



achei = texto.find('z')
if achei >= 0:
    print(f'A posição esta no indice { achei }')
else:                                                         #02
    print(f'A posição NÃO foi encontrada')


texto02 = texto.replace('aprendizado compartilhado', 'vivencia profissional')#03
print(texto02)                     # a função "replace" também faz a troca de strings 
