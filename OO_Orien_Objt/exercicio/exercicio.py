#Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e métodos para calcular a área e o
#perímetro do círculo.

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14
        
    def calculo_area(self):
        self.area = self.pi * (self.raio ** 2)
        print(f'A area é {self.area}')
    def calculo_perimetro(self):
        self.perimetro = 2 * self.pi * self.raio
        self.perimetro = round(self.perimetro, 2)
        print(f'O perimetro é {self.perimetro}')

        
p1 = Circulo(5)
p1.calculo_area()
p1.calculo_perimetro()