import random

def binary_search(data, target, low_index, high_index):
    """ Binary Search recursiva """
    if (low_index > high_index):
        return False

    mid_index = (low_index + high_index) // 2

    if target == data[mid_index]:
        return True
    elif target < data[mid_index]:
        return binary_search(data, target, low_index, mid_index - 1)
    else:
        return binary_search(data, target, mid_index + 1, high_index)


def loop_binary_search(data, target, low_index, high_index):
    """ Binary Search Iterativa """
    while(low_index < high_index):
        mid_index = (low_index + high_index) // 2
        if target == data[mid_index]:
            return True
        elif target < data[mid_index]:
            high_index = (mid_index - 1)
        else:
            low_index = (mid_index + 1)

    return False

if __name__ == "__main__":
    """ Suponga un arreglo ordenado, en el cual vamos a buscar un elemento.
    Optimizar una búsqueda en esta lista consiste en dividir la lista en partes e 
    ir comparando el número con la parte dividida, en esto consiste la búsqueda binaria.

    Se implementarán dos forma en este Script"""

    data = [random.randint(0,100) for i in range(10)]

    data.sort()

    print(data)

    target = int(input("Numero a encontrar:\t"))

    f = binary_search(data, target, 0, len(data) - 1)

    print(f)

    f = loop_binary_search(data, target, 0, len(data) - 1)

    print(f)
