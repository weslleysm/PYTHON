"""
Questão 05

• Faça a abstração de superclasse Formas Geométricas.

Obs: você deve fazer o cálculo da área e do perímetro das formas
Obs: você deve fazer quantos str forem necessarios para sua abstração

----------------------------
|    FormasGeometricas    |
----------------------------

"""

class FormasGeometricas:
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14


class CalculoArea(FormasGeometricas):
        def __init__(self, raio):
             super().__init__(raio)
             self.area = self.pi * (self.raio ** 2)
        def __str__(self) -> str:
             return f'A Area é {self.area}'
        

class CalculoPerimetro(FormasGeometricas):
    def __init__(self, raio):
        super().__init__(raio)
        self.perimetro = 2 * self.pi * self.raio
        self.perimetro = round(self.perimetro, 2)
    def __str__(self) -> str:
        return f'O Perimetro é {self.perimetro}'

        
p1 = CalculoArea(5)
print(p1)

p2 = CalculoPerimetro(10)
print(p2)