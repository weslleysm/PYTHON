class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def correr(self):
        velocidade = int(input('Informe a velocidade:'))
        if velocidade < 5:
            print(f'Sua velocidade {velocidade} estar baixa.')
        elif velocidade >= 5:
            print(f'Muito bem, voce estar coorrendo a {velocidade}Km/h.')
        return


p1 = Pessoa('weslley', 23)
print(f'Meu nome é {p1.nome}, tenho {p1.idade} anos de idade')

p1.correr()