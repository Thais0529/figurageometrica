from figurageometrica import Figurageometrica


class Rectangulo(Figurageometrica):
    def _init_(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color._init_(self, color)

    def area(self):
        return self._alto * self._ancho

    def _str_(self):
        return f"Rectángulo => {Figurageometrica.__str__(self)}, Área: {self.area()}"
