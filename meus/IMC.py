
print ("                                       Tire seu IMC")

altura = float(input("Informe sua Altura:"))
peso   = float(input("Informe seu Peso:"))

IMC = peso / (altura * altura) 

print(("Indice de Massa Corporal:"),IMC)
    
if IMC < 17:
    print("Você esta muito abaixo do peso")
elif IMC == 17 or IMC <= 18.5:
    print("Você esta abaixo do peso")
elif IMC == 18.5 or IMC <= 24.9:
    print("Seu Peso estar normal")
elif IMC == 25 or IMC <= 29.9:
    print("você esta acima do peso")
elif IMC  == 30 or IMC <= 34.9:
    print("Você esta com obesidade I")
elif IMC == 35 or IMC <= 39.9:
    print("Você esta com obesidade II(Severa)")
elif IMC >= 40:
    print("Você esta com obesidade III(Mórbio)")