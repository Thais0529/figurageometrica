from color import color
from figurageometrica import Figurageometrica

class Cuadrado(Figurageometrica, color):
    def __init__(self, lado=0, color=None):
        Figurageometrica.__init__(self, ancho=lado, alto=lado)
        color.__init__(self, nombre= color)

    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f"Cuadrado => {self.__dict__.__str__()}"

if __name__ == "__main__":
    c1= Cuadrado(lado=6, color='Rojo')
    print(c1)