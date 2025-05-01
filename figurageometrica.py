class figurageometrica:
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    def get_alto(self):
        return self._alto

    def set_alto(self, alto):
        self._alto = alto

    def get_ancho(self):
        return self._ancho

    def set_ancho(self, ancho):
        self._ancho = ancho

    def __str__(self):
        return f"Alto: {self._alto}, Ancho: {self._ancho}"


class Color:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def __str__(self):
        return f"Color: {self._color}"


class Cuadrado(figurageometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f"Cuadrado => {figurageometrica.__str__(self)}, {Color.__str__(self)}, Área: {self.area()}"


class Rectangulo(figurageometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f"Rectángulo => {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}, Área: {self.area()}"
