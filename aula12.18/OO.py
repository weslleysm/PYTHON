#                   EXEMPLO DE HERANÇA

class Estudante:# => SUPERCLASSE
    def __init__(self): # metodo contrutor
        self.nome = 'paulo'
        self.matricula = 353637
        self.nome_classe = self.__class__,__name__


class EstudanteGraducao(Estudante):# => SUBCLASSE 
    curso = 'ADS'
    def __str__(self):# metodo de imprimir 
        return f'Meu nome é {self.nome}, faço parte do curso de {self.curso} com numero de matricula {self.matricula}.'

class EstudantePos(Estudante):# => SUB CLASSE 
    nivel = 1 
    orientador = 'prof Carlos Alberto'
    def __str__(self):# metodo de imprimir 
        return f'Faço parte da {self.nome_classe} com nivel {self.nivel} e meu orientador é {self.orientador}.'


aluno1 = EstudanteGraducao()
aluno2 = EstudantePos()

print(aluno1)
print(aluno2)