# 3-faca um codigo que pede 3 notas de quatro alunos, calcule a media e printa as medias em uma lista
nota1 = int(input('informe a 1º nota do aluno 1:'))
nota2 = int(input('informe a 2º nota do aluno 1:'))
nota3 = int(input('informe a 3º nota do aluno 1:'))
aluno1 = (nota1 + nota2 + nota3) / 3
print (aluno1)

nota1 = int(input('informe a 1º nota do aluno 2:'))
nota2 = int(input('informe a 2º nota do aluno 2:'))
nota3 = int(input('informe a 3º nota do aluno 2:'))
aluno2 = (nota1 + nota2 + nota3) / 3
print(aluno2)

nota1 = int(input('informe a 1º nota do aluno 3:'))
nota2 = int(input('informe a 2º nota do aluno 3:'))
nota3 = int(input('informe a 3º nota do aluno 3:'))
aluno3 = (nota1 + nota2 + nota3) / 3
print(aluno3)

nota1 = int(input('informe a 1º nota do aluno 4:'))
nota2 = int(input('informe a 2º nota do aluno 4:'))
nota3 = int(input('informe a 3º nota do aluno 4:'))
aluno4 = (nota1 + nota2 + nota3) / 3
print(aluno4)

lista_de_medias = [ aluno1, aluno2, aluno3, aluno4]
print(lista_de_medias)