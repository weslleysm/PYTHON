# 7 faca um programa que peça uma palavra e a imprima de tras-para-frente

palavra = input('Digite uma palavra:')

for i in range(len(palavra) -1, -1, -1):
    print(palavra[i])