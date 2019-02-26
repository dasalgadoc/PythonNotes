import random

if __name__ == "__main__":
    # Ejemplos
    
    print("Listas =>")
    lista_numeros = list(range(100))

    print(lista_numeros)
    print("Transformar para obtener solo los pares")

    pares = [numero for numero in lista_numeros if numero % 2 == 0]
    print(pares)

    print("Dictionary =>")

    student_uid = [1,2,3]
    students = ['Diego','Alexander','Mayerly']

    students_with_uid = {uid: student for uid, student in zip(student_uid, students)}

    print(students_with_uid)

    print("Otro ejemplo")
    random_numbers = []
    for i in range(10):
        random_numbers.append(random.randint(1,3))

    print(random_numbers)
    print("Vamos a eliminar los repetidos con un Diccionario y una Comprehension")
    non_repeated = {element for element in random_numbers}
    
    print(non_repeated)

