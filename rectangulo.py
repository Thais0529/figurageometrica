from figurageometrica import Figurageometrica
from color import color
class Rectangulo(Figurageometrica):
    def _init_(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color._init_(self, color)

    def area(self):
        return self._alto * self._ancho

    def _str_(self):
        return f"Rectángulo => {self.__dict__.__str__()}"


if __name__ == "__main__":
    r1 = Rectangulo(alto=5,ancho=3)
    print(r1)