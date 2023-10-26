escolha = str(input("digite (+) para adição ou (-) para subtração:"))
if escolha == "+":
    print("ADIÇÃO")
    informe = int(input("informe um numero:"))
    informe2 = int(input("informe um numero:"))
    numero1 = informe + informe2
    print("TOTAL:", numero1)

elif escolha == "-":
    print("SUBTRAÇÃO")
    informe = int(input("informe um numero:"))
    informe2 = int(input("informe um numero:"))
    numero1 = informe - informe2
    print("TOTAL:", numero1)

