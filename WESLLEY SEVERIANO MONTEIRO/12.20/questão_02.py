"""
Questão 02

• Faça a abstração da superclasse Extintor de Incendio.

Obs: você deve fazer o str dela mostrando o nivel da carga do extintor

---------------------------
|    ExtintorDeIncendio   |
---------------------------

"""

class ExtintorDeIncendio:
    def __init__(self, carga_extintor, tamanho):
        self.carga_extintor = carga_extintor
        self.tamanho = tamanho
    def get_carga_extintor(self):
        return self.carga_extintor
    def get_tamanho(self):
        return self.tamanho
    
    def set_carga_extintor(self, nova_carga):
        self.carga_extintor = nova_carga
        return
    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

    def __str__(self):
        if self.carga_extintor > 10:
            return f'O Extintor {self.tamanho} está totalmete carregado'
        elif self.carga_extintor >= 5 and self.carga_extintor <= 10:
            return f'A carga do Extintor {self.tamanho} está normal'
        elif self.carga_extintor < 5:
            return f'O Extintor {self.tamanho} está com carga baixa'

p1 = ExtintorDeIncendio(5, 'Medio')
print(p1)

p1.set_carga_extintor(3)
print(p1)

p1.set_tamanho('Grande')
print(p1)