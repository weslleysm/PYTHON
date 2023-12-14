class ControleRemoto:
    def __init__(self, cor, tamanho, marca, quantidade_pilha, infla_vermelho):

        self.botao = None
        self.cor = cor 
        self.tamanho = tamanho
        self.marca = marca
        self.quantidade_pilha = quantidade_pilha
        self.infla_vermelho = infla_vermelho
        self.temperatura = 0
    # metodos 
    def ligar (self):
        self.painel = True

    def desligar (self):
        self.painel = False

    def temperatura(self, nova_temperatura):
        if self.painel == False:
            print('Temperatura não pode ser alterada')
        else: 
            self.temperatura = nova_temperatura
    
    def precionar_butao(self, tipo_de_botao):
        self.botao = tipo_de_botao
        if self.botao == 'ligar':
            print('Ar estar ligado')
            self.ligar()
        elif self.botao == 'desligar':
            print('Ar estar desligado')
            self.desligar()
    
controle = ControleRemoto('branco', 'medio', 'elgin', 2, True)

controle.temperatura(20)

controle.precionar_butao('ligar')
