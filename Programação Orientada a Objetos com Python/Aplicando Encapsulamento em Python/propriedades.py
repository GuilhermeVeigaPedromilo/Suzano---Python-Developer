# property() - Propriedades
# O decorator @property é uma maneira de usar propriedades em Python.

class Plano_Cartesiano:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
par_ordenado = Plano_Cartesiano(15, 20)
print("X: ", par_ordenado.x)
print("Y: ", par_ordenado.y)
print(f"Coordenada: {par_ordenado.x, par_ordenado.y}")

del par_ordenado
print(f"O objeto par_ordenado foi deletado: {Plano_Cartesiano().x, Plano_Cartesiano().y}")