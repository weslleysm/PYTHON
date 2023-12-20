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

class Homem(Pessoa):
    pass

class Mulher(Pessoa):
    pass

p1 = Homem('Weslley', 23)
p2 = Mulher('Livia', 24)

p1.set_cpf(123456789)
p2.set_cpf(987654321)

print(p1)
print(p2)
