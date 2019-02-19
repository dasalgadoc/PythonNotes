class Estudiante(object):
    def __init__(self,nombre_r,edad_r):
        self.nombre = nombre_r
        self.edad = edad_r

    def saludar(self):
        return "Mi nombre es {} y tengo {}".format(self.nombre, self.edad)

if __name__ == "__main__":
    e = Estudiante("Diego",27)
    print (e.saludar())


