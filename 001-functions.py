variable_global = 200
variable_global_2 = 300

def myFunction():
    return "Hello World!"


def myDefaultFunction(eName, eAge = 100):
    return "Hello, {}, you are {} years old".format(eName, eAge)


def readFunction():
    print(variable_global)


def writeFunction():
    global variable_global
    variable_global = 201

    return variable_global


def writeFunction_2():
    global variable_global
    global variable_global_2

    variable_global = 210
    variable_global_2 = 200

    return variable_global - variable_global_2


if __name__ == "__main__":

    # Parte Uno
    greeting = myFunction()
    print(greeting)

    # Parte Dos
    greetingDiego = myDefaultFunction("Diego")
    greetingDiegoAge = myDefaultFunction("Diego","27")
    print(greetingDiego)
    print(greetingDiegoAge)

    # Parte tres - Lambdas
    quickGreeting = lambda eName: "Hola, {}".format(eName)
    print(quickGreeting)

    # Parte cuatro - Globales
    readFunction()
    print(writeFunction())
    print(writeFunction_2())


