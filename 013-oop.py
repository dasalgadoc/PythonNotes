# --- HERENCIA --- #

class Perro:

    especie = 'Mamifero'

    def __init__(self, name, age):
        self.nombre = name
        self.edad = age

    def descripcion(self):
        return "{} tiene {} año(s)".format(self.nombre, self.edad)

    def ladrar(self, sound):
        return "{} dice {}".format(self.nombre, sound)


class Bulldog(Perro):
    def correr(self, speed):
        return "{} corre {}" .format(self.nombre, speed)


pedro = Bulldog("Pedro",12)
print(pedro.descripcion())
