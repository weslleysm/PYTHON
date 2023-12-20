#                               EXEMPLO DE HERANÇA

class Pessoa: #        => SUPERCLASSE
    def __init__(self, nome):# metodo de construção
        self.nome = nome
        self.sexo = 'Masculino' # parametros
        self.idade = 23   

class Estudante(Pessoa):# => SUBCLASSE
    curso = 'pedagogia'
    matricula = 1213
    def __str__(self):# metodo de imprimir
        return f'Meu nome é {self.nome} tenho {self.idade} anos, faço curso de {self.curso} e meu numero de matricula é {self.matricula}.'

class EstudantePos(Estudante):# => SUBCLASSE
    orientador = 'Prof Paulo'
    nivel = 4
    def __str__(self):# metodo de imprimir
        return f'Meu orientador se chama {self.orientador} faço curso de {self.curso} e meu nivel é {self.nivel}'


p2 = Estudante('Weslley')
print(p2)

p3 = EstudantePos('Weslley')
print(p3)