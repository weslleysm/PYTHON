class Televisao:
    def __init__(self,tamanho, canal):
        self.tamanho = tamanho
        self.canal = canal
        self.ligada = None

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def get_ligar(self):
        return self.ligada
    def get_desligar(self):
        return self.desligar
    
    def set_ligar(self, botao):
        self.ligar = botao
        if self.ligar == 'ligar':
            self.ligada = True
            print('A tv está ligada')
    def set_desligar(self, desligar):
        self.desligar = desligar
        if self.desligar == 'desligar':
            self.ligada = False
            print('A tv está desligada')

p1 = Televisao(10, 2)
p1.set_ligar('ligar')
print(p1.set_ligar)

p2 = Televisao(11, 4)
p2.set_desligar('desligar')
print(p2.set_desligar)