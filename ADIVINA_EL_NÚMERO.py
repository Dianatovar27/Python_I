import random2
import openpyxl
import getpass

excel_document= openpyxl.load_workbook("C:\\Users\\jfdr1\\Desktop\\Python_I\\Estadisticas.xlsx")
hojaSolitario = excel_document["Solitario"]
hoja2Jugadores = excel_document["2Jugadores"]

def menu():
    print("Selecciona una opcion: ")
    print("1. Partida modo solitario")
    print("2. Partida 2 Jugadores")
    print("3. Estadística")
    print("4. Salir")

def valida(min, max):
    if min > max:
        print("Error, min no puede ser mas grande que max")
    opcion = int(input())
    while opcion < min or opcion > max:
        opcion = int(input(f'Error, escribe una opción entre {min} y {max}: '))
    return opcion

def menu2():
    print("Selecciona un nivel: ")
    print("1. Fácil (20 intentos)")
    print("2. Medio (12 intentos)")
    print("3. Difícil (5 intentos)")
    print("4. Crea tu propio nivel")
    print("5. Regresar al menu principal")

def dificultadSolitario (chances, min, max):
    win=False
    numIntentado = []
    soliNumRandom=random2.giveMeNumber(min,max)
    print(f'Adivina un numero del {min} al {max}')
    while not win and chances>0:
        if len(numIntentado) == 0:
            print("Escribe tu primer numero")
        else:
            print("Estos son los numeros que has intrucido hasta el momento: " + str(numIntentado))
        adivinaSoliNum = int(input())  
        if adivinaSoliNum == soliNumRandom:
            win=True
        if adivinaSoliNum != soliNumRandom:
            chances = chances-1
            numIntentado.append(adivinaSoliNum)
            if adivinaSoliNum > soliNumRandom:
                print("El numero a adivinar es menor al intrucido")
            else:
                 print("El numero a adivinar es mayor al intrucido")
    if win:
        print(r"""
🎉 GANADOR 🎉
  __     ______  _    _  __          _______ _   _ 
  \ \   / / __ \| |  | | \ \        / /_   _| \ | |
   \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |
    \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |
     | | | |__| | |__| |    \  /\  /   _| |_| |\  |
     |_|  \____/ \____/      \/  \/   |_____|_| \_|
""")
        name= input("Escribe tu nombre porfavor: ")
        hojaSolitario.append([name, 1])
        excel_document.save("C:\\Users\\jfdr1\\Desktop\\Python_I\\Estadisticas.xlsx")
    else:
        print("""
╔═══╗ ♪
║███║ ♪
║ (╯︵╰) Has perdido! Fin del juego...
╚═══╝
""")
        print("El numero era: " + str(soliNumRandom))
        name= input("Escribe tu nombre porfavor: ")
        hojaSolitario.append([name, None, None])
        excel_document.save("C:\\Users\\jfdr1\\Desktop\\Python_I\\Estadisticas.xlsx")

def dificultadPropioNivelSolitario():
    chances= int(input("Elije el numero de intentos: "))
    print("Ahora escoge el rango")
    min = int(input("Elije el numero menor: "))
    max = int(input("Elije el numero mayor: "))
    while min > max:
        print("Error el numero menor no puede ser mas grande que el mayor")
        min = int(input("Elije el numero menor: "))
        max = int(input("Elije el numero mayor: "))

    dificultadSolitario (chances,min,max)

def dificultad2Jugadores (chances):
    win=False 
    num2JugadoresIntentado= []

    print("Bienvenidos a la partida para 2 jugadores.\nJugador numero 1 escribira un número entre el 1 y el 1000, jugador numero dos intentara adivinarlo")
    NumJugador1 = int(getpass.getpass("Jugador número 1, introduce el número a adivinar (no te preocupes, el numero no se mostrara en pantalla): "))

    while NumJugador1 < 1 or NumJugador1 > 1000:
        NumJugador1 = int(getpass.getpass("Error, escribe un numero entre 1 y 1000: "))

    while not win and chances>0:
        if len(num2JugadoresIntentado) == 0:
            print("Jugador 2 escribe tu primer numero: ")
        else:
            print("Estos son los numeros que has intrucido hasta el momento: " + str(num2JugadoresIntentado))
        NumJugador2 = int(input())  
        if NumJugador2 == NumJugador1:
            win=True
        if NumJugador2 != NumJugador1:
            chances = chances-1
            num2JugadoresIntentado.append(NumJugador2)
            if NumJugador2 > NumJugador1:
                print("El numero a adivinar es menor al intrucido")
            else:
                 print("El numero a adivinar es mayor al intrucido")
    if win:
        print(r"""
🎉 GANADOR 🎉
  __     ______  _    _  __          _______ _   _ 
  \ \   / / __ \| |  | | \ \        / /_   _| \ | |
   \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |
    \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |
     | | | |__| | |__| |    \  /\  /   _| |_| |\  |
     |_|  \____/ \____/      \/  \/   |_____|_| \_|
""")
        name= input("Jugador 2 Escribe tu nombre porfavor: ")
        hoja2Jugadores.append([name, 1])
        excel_document.save("C:\\Users\\jfdr1\\Desktop\\Python_I\\Estadisticas.xlsx")
    else:
        print("""
╔═══╗ ♪
║███║ ♪
║ (╯︵╰) Has perdido! Fin del juego...
╚═══╝
""")
        print("El numero era: " + str(NumJugador1))
        name= input("Jugador 2 Escribe tu nombre porfavor: ")
        hoja2Jugadores.append([name, None, 1])
        excel_document.save("C:\\Users\\jfdr1\\Desktop\\Python_I\\Estadisticas.xlsx")

def dificultadPropio2jugadores():
    print("Bienvenidos a la partida para 2 jugadores.\nJugador numero 1 escribira un número y el jugador numero 2 intentara adivinarlo")
    chancesPropio2= int(input("Primero escribe el numero de intentos que tiene jugador 2 para adivinar: "))
    win=False
    numIntentadoPropio2 = []
    print("Ahora escoge el rango")
    minPropio2 = int(input("Elije el numero menor: "))
    maxPropio2 = int(input("Elije el numero mayor: "))
    while minPropio2 > maxPropio2:
        print("Error el numero menor no puede ser mas grande que el mayor")
        minPropio2 = int(input("Elije el numero menor: "))
        maxPropio2 = int(input("Elije el numero mayor: "))

    PropioNumJugador1 = int(getpass.getpass("Jugador número 1, introduce el número a adivinar (no te preocupes, el numero no se mostrara en pantalla): "))

    while PropioNumJugador1 < minPropio2 or PropioNumJugador1 > maxPropio2:
        PropioNumJugador1 = int(getpass.getpass("Error, escribe un numero dentro el rago seleccionado anteriorment: "))

    while not win and chancesPropio2>0:
        if len(numIntentadoPropio2) == 0:
            print("Jugador 2 escribe tu primer numero: ")
        else:
            print("Estos son los numeros que has intrucido hasta el momento: " + str(numIntentadoPropio2))
        PropioNumJugador2 = int(input())  
        if PropioNumJugador2 == PropioNumJugador1:
            win=True
        if PropioNumJugador2 != PropioNumJugador1:
            chancesPropio2 = chancesPropio2-1
            numIntentadoPropio2.append(PropioNumJugador2)
            if PropioNumJugador2 > PropioNumJugador1:
                print("El numero a adivinar es menor al intrucido")
            else:
                 print("El numero a adivinar es mayor al intrucido")
    if win:
        print(r"""
🎉 GANADOR 🎉
  __     ______  _    _  __          _______ _   _ 
  \ \   / / __ \| |  | | \ \        / /_   _| \ | |
   \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |
    \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |
     | | | |__| | |__| |    \  /\  /   _| |_| |\  |
     |_|  \____/ \____/      \/  \/   |_____|_| \_|
""")
        name= input("Jugador 2 Escribe tu nombre porfavor: ")
        hoja2Jugadores.append([name, 1])
        excel_document.save("C:\\Users\\jfdr1\\Desktop\\Python_I\\Estadisticas.xlsx")
    else:
        print("""
╔═══╗ ♪
║███║ ♪
║ (╯︵╰) Has perdido! Fin del juego...
╚═══╝
""")
        print("El numero era: " + str(PropioNumJugador1))
        name= input("Jugador 2 Escribe tu nombre porfavor: ")
        hoja2Jugadores.append([name, None, 1])
        excel_document.save("C:\\Users\\jfdr1\\Desktop\\Python_I\\Estadisticas.xlsx")

while True:
    opcionMenu1 = 0
    menu()
    opcionMenu1 = valida(1, 4)

    if opcionMenu1 == 4:
        break

    if opcionMenu1 == 1:
        menu2()
        opcionMenu2 = valida(1, 5)
        if opcionMenu2 == 1:
            dificultadSolitario (20,1,1000)
        if opcionMenu2 == 2:
            dificultadSolitario (12,1,1000)
        if opcionMenu2 == 3:
            dificultadSolitario (5,1,1000)
        if opcionMenu2 == 4:
            dificultadPropioNivelSolitario()
        
    if opcionMenu1 == 2:
        menu2()
        opcionMenu2 = valida(1,5)
        if opcionMenu2 == 1:
            dificultad2Jugadores (20)
        if opcionMenu2 == 2:
            dificultad2Jugadores (12)
        if opcionMenu2 == 3:
            dificultad2Jugadores (4)
        if opcionMenu2 == 4:
            dificultadPropio2jugadores()







     

        




