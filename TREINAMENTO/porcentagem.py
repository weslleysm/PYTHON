# 3. Crie um código que receba o salário atual de um funcionário, que receba o valor em porcentagem de reajuste e 
# calcule o valor do novo salário reajustado de acordo com valor de reajuste(%).

# porcentagem (porcentagem )
salario = float(input('Informe o seu salario:'))
porcentagem = int(input('Informe a porcentagem que voce vai ganhar:'))
reajuste = (porcentagem * salario) / 100
novo_salrio = salario + reajuste
print(f'o reajuste e de ${reajuste} totalizando o seu novo salario em ${novo_salrio}')