from figurageometrica import Figurageometrica


class Cuadrado(Figurageometrica):
    def _init_(self, lado, color):
        Figurageometrica.__init__(self, lado, lado)


    def area(self):
        return self._alto * self._ancho

    def _str_(self):
        return f"Cuadrado => {figurageometrica.__str__(self)}, Área: {self.area()}"