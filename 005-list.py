import copy

if __name__ == "__main__":
    
    # Inicializando Listas
    print("Inicializando listas =>")
    vacia = []
    print(vacia)

    numeros = [1,2,3]
    print(numeros)

    funcional_vacia = list()
    print(funcional_vacia)

    pares = list(range(0,10,2))
    print(pares)
    
    # Copiar Listas
    print("Copiando una lista =>")
    copiar_pares = copy.copy(pares)
    print(copiar_pares)

    # Iterando sobre listas
    print("Imprimienmdo una list =>")

    numeros = ['UNO','DOS','TRES','CUATRO','CINCO']

    for numero in numeros:
        print(numero)

    # Operaciones con Listas
    print("Operaciones con Listas =>")

    impares = list(range(1,10,2))
    print(pares)
    print(impares)

    print(pares + impares)

    print(pares * 5)

    # Append
    
    print("Append en listas =>")
    print(numeros)
    numeros.append("SEIS")
    print(numeros)
    
    # Pop

    print("Pop en listas =>")
    print(numeros)
    numeros.pop()
    print(numeros)

    numeros.pop(2)
    print(numeros)

    # Del
    
    print("Del en listas =>")
    hasta_quince = list(range(0,16))
    print(hasta_quince)

    del hasta_quince[11:]
    print(hasta_quince)

    # Remove
    print("Remove en listas =>")
    print(numeros)
    
    numeros.remove("UNO")
    print(numeros)

    # Sorted

    print("Sorted en listas =>")
    print(pares)
    print(impares)

    hasta_diez = pares + impares

    print(hasta_diez)
    
    print(sorted(hasta_diez))

    print(sorted(hasta_diez,reverse = True))

    print(hasta_diez)

    # Sort

    print("Sort en listas =>")
    print(hasta_diez)

    hasta_diez.sort()
    print(hasta_diez)
    
    hasta_diez.sort(reverse = True)
    print(hasta_diez)

    
