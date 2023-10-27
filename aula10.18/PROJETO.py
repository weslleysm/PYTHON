print("                                      MINI TABUADA")
print("Informe abaixo qual operação voce deseja executar")
print("(1)Adição (2)Subtração (3)Divisão (4)Multiplicação ")

escolha = str(input("Informe aqui:"))

if escolha == "1" or escolha == "adição" or escolha == "Adição" or escolha == "ADIÇÃO":
    print("ADIÇÃO")
    informe = int(input("Numero:"))
    informe2 = int(input("Mais:"))
    numero1 = informe + informe2
    print("TOTAL:", numero1)

elif escolha == "2" or escolha == "subtração" or escolha == "Subtração" or escolha == "SUBTRAÇÃO ":
    print("SUBTRAÇÃO")
    informe = int(input("Numero:"))
    informe2 = int(input("Menos:"))
    numero1 = informe - informe2
    print("TOTAL:", numero1)



elif escolha == "3" or escolha == "divisão" or escolha == "Divisão" or escolha == "DIVISÃO ":
    print("DIVISÃO")
    informe = int(input("Numero:"))
    informe2 = int(input("Dividido:"))
    numero1 = informe / informe2
    print("TOTAL:", numero1)

elif escolha == "4" or escolha == "multiplicação" or escolha == "Multiplicação" or escolha == "MULTIPLICAÇÃO ":
    print("MULTIPLICAÇÃO")
    informe = int(input("numero:"))
    informe2 = int(input("Vezes:"))
    numero1 = informe * informe2
    print("TOTAL:", numero1)

else:
    print("Operador não indentificado")

