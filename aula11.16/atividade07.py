# peça três temperaturas coloque em uma lista
# caso seja igual ou maior que 38 graus avisar que está com febre
# adicione duas novas temperaturas
# delete a temperatura do segundo indice
# delete a ULTIMA temperatura
# imprima os resultados

temperatura = int(input("Temperatura: "))
if temperatura >= 38 :
    print("Você está com febre")
temperatura2 = int(input("Temperatura: "))
if temperatura2 >= 38 :
    print("Você está com febre")
temperatura3 = int(input("Temperatura: "))
if temperatura3 >= 38 :
    print("Você está com febre")

lista_temp = [temperatura, temperatura2, temperatura3]

lista_temp.append(15)
lista_temp.append(16)
del lista_temp[1]
del lista_temp[-1]
print(lista_temp)
