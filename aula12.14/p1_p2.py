from OO import Pessoa
def linha():
    print(60*'-')

p1 = Pessoa('weslley', 23)
p2 = Pessoa('Livia', 24)
linha()

p1.falar('Estudos')
p1.comer('laranja')
p1.parar_falar()
p1.comer('laranja')
p1.falar('Escola')
p1.parar_comer()
p1.falar('Escola')
linha()

p2.comer('Abacaxi')
p2.falar('algo')
p2.parar_comer()
p2.falar('Estudos')