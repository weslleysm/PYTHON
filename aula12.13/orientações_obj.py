from collections.abc import Iterable

def linha():
    print(60*'-')

class Automovel:
    def __init__(self, placa, cor):
        self.placa = placa
        self.cor = cor
    def get_placa(self):# get_ serve para chamar, não se altera
        return self.placa
    def dirigir (self, velocidade):
        print(f'Estou dirigindo a {velocidade}Km/h')
    def get_cor(self):
        return self.cor
    def set_cor(self, nova_cor):# set_ chama e pode ser alterado
        self.cor = nova_cor
    
linha()
carro = Automovel('DHA-3568', 'preto')
print(carro.get_cor())
print(carro.get_placa())
carro.dirigir(220)
linha()
moto = Automovel('WEB-1510', 'verde')
print(moto.get_placa())
carro.dirigir(70)
linha()