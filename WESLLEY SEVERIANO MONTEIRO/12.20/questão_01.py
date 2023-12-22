"""
Questão 01

• Faça a abstração da superclasse Veículo. Você deve ter pelo menos duas subclasses, nove atributos e 12 metodos.

Obs: você deve fazer o str de cada uma delas

------------------
|    Veiculos    |
------------------

"""

class Veiculos():
    def __init__(self,placa, cor):
        self.placa = placa
        self.cor = cor 
    def __str__(self):
        return f'Placa: {self.placa}, Cor: {self.cor}'
    
    def get_placa(self):
        return self.placa    # 4
    def get_cor(self):
        return self.cor
    
    def set_placa(self, nova_placa):
        self.placa = nova_placa
    def set_cor(self,nova_cor):
        self.cor = nova_cor


class Carro(Veiculos):
    def __init__(self, placa, cor, modelo, marca, ):
        super().__init__(placa, cor)
        self.modelo = modelo
        self.marca = marca    #4
    def __str__(self):
        return f'Placa: {self.placa}, Cor: {self.cor}, Modelo: {self.modelo}, Marca: {self.marca}'
    
    def get_modelo(self):
        return self.modelo
    def get_marca(self):
        return self.marca
    
    def set_modelo(self, nova_modelo):
        self.modelo = nova_modelo
    def set_marca(self, nova_marca):
        self.marca = nova_marca

class Motocicleta(Veiculos):
    def __init__(self, placa, cor, velocidade):
        super().__init__(placa, cor)
        self.velocidade = velocidade
    def __str__(self):
        return f'Minha moto da Cor {self.cor} e Placa {self.placa}, está a {self.velocidade}Km/h.'
    
    def get_velocidade(self):
        return self.velocidade
    def set_velocidade(self, nova_velocidade):
        self.velocidade = nova_velocidade 

p1 = Veiculos('ABCD', 'Verde')
print(p1)
carro = Carro('POIU', 'Azul', 'Uno', 'Fiat')
print(carro)
moto = Motocicleta('FGHJ', 'Preto', 200)
print(moto)
