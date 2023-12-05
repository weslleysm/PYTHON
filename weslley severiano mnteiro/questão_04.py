"""
Questão 04

• Escreva um programa que atenda as requisições abaixo e imprima todos os resultados:

01. crie uma função que faça a troca de caracteres de acordo com a escolha do usuario. Imprima em uma nova string.
02. utilizando um FOR troque os espaços em branco por -.

"""

texto = "Neste curso, os alunos(as) terão capacidades para trabalharem com toda a estrutura de dados que roda por trás de aplicações web. Compreendendo as necessidades de geração, captura e armazenamento de dados de uma aplicação web e a desenvolve, levando sempre em consideração a agilidade, segurança e confiabilidade nos dados que serão gerados e, por vezes, integrados a outros sistemas de gestão estratégica."

#replace - é utilizado para realiar alterações dentro das strings, e mudar uma caractere por outra
adicionar = input("qual caractere voçe deseja remover do texo? ")
remover = input("qual caractere deseja adicionar no texto: ")
novo_texto = texto.replace(adicionar,remover)
for i in novo_texto:
    novo_texto2 = novo_texto.replace(" ","-")
print(novo_texto2) 