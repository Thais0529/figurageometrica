from Color import Color
from Figurageometrica import figurageometrica

class Cuadrado(Figurageometrica, Color):
    def __init__(self, lado=0, color=None):
        Figurageometrica.__init__(self, ancho=lado, alto=lado)  # ambos lados iguales en un cuadrado
        Color.__init__(self,nombre= color)

    def area(self):
        return self.alto * self.alto

    def __str__(self):
        return f"Cuadrado -> {self.__dict__.__str__()}"

if __name__ == "__main__":
    c1 = Cuadrado(lado=6, color= "Rojo")
    print(c1)
    print(f'Area:{c1.area()}')
    print(f'Perimetro: {c1.perimetro()}')