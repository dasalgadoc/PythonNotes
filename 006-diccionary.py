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
    

    print("Llamado de elementos =>")
    print(precios['huevo'])

    # Usando funciones en diccionarios
    print("Usando funciones en diccionarios =>")

    print(precios.keys())
    print(precios.values())
    print(precios.items())
