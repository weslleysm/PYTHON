def espaco():
    print(100*'_')

# Crie abstração para uma super classe funcionario com duas subclasses. Imprima todos os dados

class Funcionario:#                          superclasse
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'

class FuncionarioTatico(Funcionario):#      subclasse
    def __init__(self, nome, idade, cargo, funcao):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.funcao = funcao
    def __str__(self):
        return f'Meu nome é {self.nome}, tenho {self.idade} anos, sou {self.cargo} e minha função é {self.funcao}'
class FuncionarioOperacional(Funcionario):# subclasse
    def __init__(self, nome, idade, cargo, funcao, carga_horaria):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.funcao = funcao
        self.carga_horaria = carga_horaria
    def __str__(self):
        return f'Sou {self.nome}, tenho {self.idade} anos, sou {self.cargo}, trabalho {self.carga_horaria}h por dia e minha função é {self.funcao}'

espaco()
f = Funcionario('Weslley', 23)
print(f)
espaco()
f_tatico = FuncionarioTatico('Livia', 24, 'Gerente', 'Administrar a Empresa')
print(f_tatico)
espaco()
f_operacional = FuncionarioOperacional('Weslley', 23, 'Vendedor', 'Vender Roupas', 10)
print(f_operacional)
espaco()