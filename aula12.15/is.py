class Pet:
    def __init__(self,nome, peso):
        self.nome = nome
        self.peso = peso
        self.fome = 0
        self.comida = 100

    #os GET
    def get_nome(self):
        return self.nome
    def get_peso(self):
        return self.peso
    def get_fome(self):
        return self.fome
    
    #os SET
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def set_peso(self, novo_peso):
        self.peso = novo_peso
    def set_fome(self, novo_fome):
        self.fome += novo_fome
        while self.fome >= 99:
            print(f'Alimente a/o {self.nome}')
            nova_comida = int(input(f'quanto de comida voce quer da pro seu Pet?'))
            print(f'Minha fome esta em {self.fome}')
            self.comida -= nova_comida
            self.fome -= nova_comida

    def imprimir(self):
        print(f'Olá, me chamo {self.nome}')
        print(f'Estou pesando {self.peso}kg')
        print(f'Minha fome esta em {self.fome}')

#instancias
caozinho = Pet('Bodo', 15)

caozinho.imprimir()
caozinho.set_fome(20)
caozinho.imprimir()

caozinho.imprimir()
caozinho.set_fome(30)
caozinho.imprimir()

caozinho.imprimir()
caozinho.set_fome(70)
caozinho.imprimir()

caozinho.imprimir()
caozinho.set_fome(10)
caozinho.imprimir()
