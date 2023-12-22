class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome 
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} ja está falando')
            return
        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True
        
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} nao esta falando')
            return
        print(f'{self.nome} parou de falar.')
        self.falando = False



    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} ja estar comendo')
            return
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return
        print(f'{self.nome} está comento {alimento}.')
        self.comendo = True
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False



#INSTANCIAS

p1 = Pessoa('weslley', 23)#atribui o valor
p1.comer('maça')#mandei a pessoa comer
p1.parar_comer()#mandei parar de comer
p1.parar_comer()#mandei parar de comer novamente
p1.comer('maca')#mandei a pessoa comer novamente

p2 = Pessoa('livia', 24)# atribui o valor de p2
p2.comer('laranja')#mandei ela comer
p2.falar('escola')#mandei ela falar, porem vai da mensagem de erro por que não pode falar comendo
p2.parar_comer()#mandei ela parar de come, para poder falar
p2.falar('escola')#mandei ela falar
p2.comer('alimento')# mandei ela comer, porém ela nao pode comer pq está falando
p2.parar_falar()#mandei ela parar de falar
p2.comer('alimento')# mandei ela comer novamente, agora ela pode comer 