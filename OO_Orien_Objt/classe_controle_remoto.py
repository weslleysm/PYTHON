class ControleRemoto:
    def __init__(self, cor, marca, quantidade_pilha):

        self.botao = None
        self.cor = cor 
        self.marca = marca
        self.quantidade_pilha = quantidade_pilha
        self.painel = False
        self.temperatura = 0
    # metodos 
    def ligar (self):
        self.painel = True

    def desligar (self):
        self.painel = False

    def set_temperatura(self, nova_temperatura):
        if self.painel == False:
            print('Temperatura não pode ser alterada')
        else: 
            self.temperatura = nova_temperatura

    def get_temperatura(self):
        return self.temperatura
    
    def pressionar_botao(self, tipo_de_botao):
        self.botao = tipo_de_botao
        if self.botao == 'ligar' and self.temperatura == 0:
            print('Ar estar ligado')
            self.ligar()
        elif self.botao == 'desligar':
            print('Ar estar desligado')
            self.set_temperatura(0)
            self.desligar()
    
#INSTANCIAS
controle = ControleRemoto('branco', 'elgin', 2)

controle.pressionar_botao('ligar')

controle.set_temperatura(18)

print(controle.get_temperatura())

controle.pressionar_botao('desligar')
controle.pressionar_botao('ligar')

controle.set_temperatura(20)

print(controle.get_temperatura())