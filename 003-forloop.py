
if __name__ == "__main__":
    
    cadena = "Hola, Mundo"

    print("Imprimir Cadena")
    print(cadena)

    print("Imprimir Caracter por Caracter")
    for caracter in cadena:
        print(caracter)

    print("Imprimir lista =>")

    for entero in range(10):
        print(entero)

    # Secuencias de ruptura
    print("Imprimir Secuencias de Ruptura =>")

    for i in range(35):
        if i > 30 and i < 32:
            break

        # Si el número entre 1 y 35 es par
        if i % 2 == 0:
            print(i, end=" ")
        else:
            continue
            print("Print Inalcanzable")
