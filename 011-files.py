import csv
import os

FILE_NAME = '011-filesA.txt'
FILE_NAME_CSV = '011-filesB.csv'
LLAVES = ['nombre','profesion','edad']
Personas = list()

def readFile():
    # Uso de archivos planos
    with open(FILE_NAME, mode='r') as f:
        for line in f:
            print (line)
    

def writeFile():
    with open(FILE_NAME, mode='w') as f:
        f.write("Linea 4: Hold the Line")
        f.close()


def readCSV():
    with open(FILE_NAME_CSV, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=LLAVES)
        for row in reader:
            Personas.append(row)
        f.close()


def writeCSV(Agenda):
    Agenda_Temporal = "{}.tmp".format(FILE_NAME_CSV)
    with open(Agenda_Temporal, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=LLAVES)
        writer.writerow(Agenda)
        
        os.remove(FILE_NAME_CSV)
        os.rename(Agenda_Temporal, FILE_NAME_CSV)
        f.close()
    


def main():
    
    # Impresión archivo plano

    readFile()
    print("Escribiendo sobre el archivo =>")
    writeFile()
    readFile()

    #Usar Diccionarios
    print("Escrbriendo sobre archivo CSV")
    Agenda = {'nombre': 'Diego',
            'profesion': 'Ingeniero',
            'edad': 27}
    
    readCSV()
    print(Personas)
    print(Agenda)
    writeCSV(Agenda)
    readCSV()


if __name__ == "__main__":
    main()
