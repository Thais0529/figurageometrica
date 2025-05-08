class Figurageometrica:
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

if __name__ == "__main__":
    fig1 = Figurageometrica(ancho=5,alto=6)
    print(fig1)


