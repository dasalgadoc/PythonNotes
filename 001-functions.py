def myFunction():
    return "Hello World!"

def myDefaultFunction(eName, eAge = 100):
    return "Hello, {}, you are {} years old".format(eName, eAge)


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


