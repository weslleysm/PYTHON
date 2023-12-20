class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__cpf = None

    def __str__(self):
        return f'Nome: {self.nome}, Idade:{self.idade} e CPF: {self.__cpf}'
    
    def get_cpf(self):
        return self.__cpf
    def set_cpf(self, meu_cpf):
        self.__cpf = meu_cpf

class Professor(Pessoa):
    def __init__(self, nome, idade, salario, disciplina):
        super().__init__(nome, idade,)
        self.salario = salario
        self.disciplina = disciplina 
    def __str__(self):
        return f'Nome: {self.nome}, Idade:{self.idade}, Salario: {self.salario} e Disciplina: {self.disciplina}'
      
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, ):
        super().__init__(nome, idade)
        self.curso = curso
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}'

p = Pessoa('jo', 20)
p.set_cpf(1234567)
print(p)

p1 = Professor('Weslley', 23, 1300, 'pedagogia')
print(p1)

p2 = Aluno('João', 26, 'programador')
p2.set_cpf(98765432)
print(p2.__cpf)
print(p2)