def linha():
    print(60*'-')
#                        pass serve para passar sem da erro
class Automovel:
    def __init__(self, placa, cor):
        self.placa = placa
        self.cor = cor
    def get_placa(self):# get_ serve para chamar, não se altera
        return self.placa
    def get_cor(self):
        return self.cor
    
    def set_cor(self, nova_cor):# set_ chama e pode ser alterado
        self.cor = nova_cor
    def dirigir (self, velocidade):
        print(f'Estou dirigindo a {velocidade}Km/h')

# Instancia
carro = Automovel('DHA-3568', 'preto')
moto = Automovel('WEB-1510', 'vermelho')
caminhao = Automovel('ZYK-5454', 'cinza')

#chamadas GET
linha()
print(f'A cor do carro é {carro.get_cor()}')
print(f'A placa do carro é {carro.get_placa()}')
carro.dirigir(100)
linha()
print(f'A cor da moto é {moto.get_cor()}')
print(f'A placa da moto é {moto.get_placa()}')
moto.dirigir(70)
linha()
print(f'A cor do caminhão é {caminhao.get_cor()}')
print(f'A placa do caminhão é {caminhao.get_placa()}')
moto.dirigir(200)
linha()

#chamadas SET
carro.set_cor('branco')
moto = Automovel('WEB-1510', 'dourado')
caminhao = Automovel('ZYK-5454', 'azul')
print(f'O carro foi pintado para {carro.set_cor()}')

