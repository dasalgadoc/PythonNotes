if __name__ == "__main__":
    # Inicializando conjuntos
    print("Inicializando conjuntos =>")
    
    numeros = {1,2,3}
    print(numeros)

    vacio = set()
    print(vacio)

    impares = set([1,2,3])
    print(impares)
    
    # Añadir elementos
    print("Añadir elementos =>")

    print(impares)
    impares.add(4)
    print(impares)

    impares.update([5,6,7])
    print(impares)

    impares.update([8,9],{10})
    print(impares)


    # Remover elementos
    print("Remover elementos =>")
    print(impares)

    impares.remove(10)
    print(impares)

    impares.discard(8)
    print(impares)
    
    impares.clear()
    print(impares)

    # Operaciones con conjuntos
    print("Operaciones con conjuntos =>")

    A = {1,2,3,4,5}
    B = {4,5,6,7,8}

    print(A)
    print(B)

    print("Union")
    print(A.union(B))
    print(A | B)

    print("Interseccion")
    print(A.intersection(B))
    print(A & B)

    print("Diferencia")
    print(A.difference(B))
    print(B - A)

    print("Diferencia simetrica")
    print(A.symmetric_difference(B))
    print(A ^ B)

