class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes
        
    def dar_likes(self):
        self.__likes += 1
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


vingadores = Filme('Vingadores - Guerra infinita', 2018, 160)
vingadores.dar_likes() # dei um like pro filme
print(f'Nome: {vingadores.nome}, Ano: {vingadores.ano}, Duração: {vingadores.duracao}, Likes: {vingadores.likes}')

atlanta = Serie(f'Atlanta', 2017, 2)
atlanta.dar_likes()
atlanta.dar_likes()# dei dois likes pra serie
print(f'Nome: {atlanta.nome}, Ano: {atlanta.ano}, Temporada: {atlanta.temporadas}, Likes: {atlanta.likes}')