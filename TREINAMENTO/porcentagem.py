# 3. Crie um código que receba o salário atual de um funcionário, que receba o valor em porcentagem de reajuste e 
# calcule o valor do novo salário reajustado de acordo com valor de reajuste(%).

# porcentagem (porcentagem )
salario_atual = float(input('informe seu salario atual:'))
porcentagem = int(input('informe o valor da nova porcentagem:'))

valor_porcentagem = (porcentagem * salario_atual) / 100
novo_salario = salario_atual + valor_porcentagem
print(f'o valor da porcentagem de {porcentagem}% do seu salario é {valor_porcentagem} e o seu novo salario vai ser {novo_salario}')