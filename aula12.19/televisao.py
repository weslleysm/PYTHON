class Televisao:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.canal = 0
        self.ligada = False
    
    # gets
    def get_tamanho(self):
        return self.tamanho
    def get_canal(self):
        return self.canal
    # sets
    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
    def set_canal(self, novo_canal):
        if self.ligada == True and novo_canal >= 0 and novo_canal <= 999:
             self.canal = novo_canal
        
#propios
    def ligar(self):
        self.ligada = True
        print('sua tv esta ligada')
    def desligar(self):
        self.ligada = False
        print('sua tv esta desligada')
    def valida_ligada(self):
        if self.ligada == True:
            return 'Ligado'
        else:
            return 'Desligar'
    def passar(self):
        if self.ligada == True:
            print('passar de canal')
        elif self.ligada == False:
            print('A TV esta desligada')
    def __str__(self):
        return f'Sua TV está { self.valida_ligada() } o canal está em { self.canal } e o tamanho dela é { self.tamanho } polegadas'

minha_tv = Televisao(32)

minha_tv.ligar()
minha_tv.desligar()
minha_tv.passar()

minha_tv.ligar()
minha_tv.passar()
minha_tv.set_canal(10)

print(minha_tv.get_canal())

print(minha_tv)