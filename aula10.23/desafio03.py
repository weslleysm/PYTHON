# 3. Crie um código que receba o salário atual de um funcionário, que receba o valor em porcentagem de reajuste e 
# calcule o valor do novo salário reajustado de acordo com valor de reajuste(%).

# porcentagem (porcentagem )


salario_atual = int(input("Informe o salario: "))
reajuste      = int(input("Informe a porcentagem em reajuste: "))

porcentagem  = reajuste * salario_atual / 100
novo_salario = salario_atual + porcentagem

print ("O novo salario é:", novo_salario)
