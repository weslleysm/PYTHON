# O * e o simbolo de desempacotamento dentro do parametro, voce informa ao Python que vai passar varios parametros 

def contador (* num):
    tam = len(num)
    print(f'Recebi os valores {num} que são ao todo {tam} numeros.')

contador(1,4, 6, 9)
contador(10, 20, 30)
contador(0, 4, 5)
contador(5)