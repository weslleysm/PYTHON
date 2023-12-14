from OO import Pessoa


# atribui o valor de p2
p2 = Pessoa('livia', 24)

#mandei ela comer
p2.comer('laranja')

#mandei ela falar, porem vai da mensagem de erro por que não pode falar comendo
p2.falar('escola')

#mandei ela parar de come, para poder falar
p2.parar_comer()

#mandei ela falar
p2.falar('escola')

# mandei ela comer, porém ela nao pode comer pq está falando
p2.comer('alimento')

#mandei ela parar de falar
p2.parar_falar()

# mandei ela comer novamente, agora ela pode comer 
p2.comer('alimento')
