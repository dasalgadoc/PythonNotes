if __name__ == "__main__":
    # Inicianlizando Diccionarios
    
    print("Inicializando Diccionarios =>")

    vacio = {}
    print(vacio)
    print(type(vacio))

    precios = {'leche': 2500,
                'huevo': 300,
                'pan': 300}
    
    print(precios)
    
    funcional = dict()
    print(funcional)
    print(type(funcional))
    
    persona = dict({'nombre':'Diego', 'cargo': 'Ingeniero'})
    print(persona)

    almuerzo = dict([('principio','arroz'), ('proteina','pollo')])
    print(almuerzo)

    print("Llamado de elementos =>")
    print(precios['huevo'])

    # Añadir Elemento
    print("Añadir un elemento =>")
    print(almuerzo)
    almuerzo['ensalada'] = 'aguacate'
    print(almuerzo)

    # Usando funciones en diccionarios
    print("Usando funciones en diccionarios =>")

    print(precios.keys())
    print(precios.values())
    print(precios.items())

    # Eliminar elementos
    print("Eliminar elementos =>")
    print(almuerzo)

    almuerzo.pop('principio')
    print(almuerzo)
    
    almuerzo.clear()
    print(almuerzo)
