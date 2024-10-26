import lib_adivina
import openpyxl
import getpass

lib_adivina.welcome()
print('Hola! Bienvenido a Adivina el Numero. Antes de comenzar a jugar hagamos un pequeno set up:')

ubicacion_archivo = input(f'Porfavor Ingresa la ruta donde quieres guardar Estadisticas.xlsx (ej., C:\\Users\\TuUsuario\\Desktop\\):  ')
excelDocument = openpyxl.Workbook()

hojaSolitario = excelDocument.active
hojaSolitario.title = "Solitario"
hojaSolitario.append(["Nombre", "Nivel", "Ganadas"])

hoja2Jugadores = excelDocument.create_sheet(title="2Jugadores")

hoja2Jugadores.append(["Nombre", "Nivel", "Ganadas"])

excelDocument.save(f"{ubicacion_archivo}\\Estadisticas.xlsx")
print("⭐️⭐️⭐️¡Archivo guardado exitosamente!⭐️⭐️⭐️")

def menu():
    lib_adivina.Menu()
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
    lib_adivina.nivel()
    print("Selecciona un nivel: ")
    print("1. Fácil (20 intentos)")
    print("2. Medio (12 intentos)")
    print("3. Difícil (5 intentos)")
    print("4. Crea tu propio nivel")
    print("5. Regresar al menu principal")

def jugarSolitario (chances, min, max):
    if chances == 20 and min == 1 and max == 1000:
        nivel= "Fácil"
    elif chances == 12 and min == 1 and max == 1000:
        nivel= "Medio"
    elif chances == 5 and min == 1 and max == 1000:
        nivel= "Difícil"
    else:
        nivel = "Propio"
    win=False
    numIntentado = []
    soliNumRandom=lib_adivina.giveMeNumber(min,max)
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
        lib_adivina.win()
        name= input("Escribe tu nombre porfavor: ")
        hojaSolitario.append([name, nivel, 1])
      
    else:
        lib_adivina.lose()
        print("El numero era: " + str(soliNumRandom))
        name= input("Escribe tu nombre porfavor: ")
        hojaSolitario.append([name, nivel, None])
    
    excelDocument.save(f"{ubicacion_archivo}\\Estadisticas.xlsx")
      

def jugarSolitarioPropioNivel():
    chances= int(input("Elije el numero de intentos: "))
    print("Ahora escoge el rango")
    min = int(input("Elije el numero menor: "))
    max = int(input("Elije el numero mayor: "))
    while min > max:
        print("Error el numero menor no puede ser mas grande que el mayor")
        min = int(input("Elije el numero menor: "))
        max = int(input("Elije el numero mayor: "))

    jugarSolitario (chances,min,max)

def jugar2Jugadores(chances, min, max, chancesPropio=False):
    if chancesPropio:
        chances = int(input("Primero escribe el número de intentos para jugador 2: "))
        min = int(input("Elije el número menor: "))
        max = int(input("Elije el número mayor: "))
        while min > max:
            print("Error, el número menor no puede ser mayor al mayor")
            min = int(input("Elije el número menor: "))
            max = int(input("Elije el número mayor: "))

    if chances == 20 and min == 1 and max == 1000:
        nivel= "Fácil"
    elif chances == 12 and min == 1 and max == 1000:
        nivel= "Medio"
    elif chances == 5 and min == 1 and max == 1000:
        nivel= "Difícil"
    else:
        nivel = "Propio"
    win = False
    numIntentado = []
    print(f"Bienvenidos a la partida para 2 jugadores.\nJugador número 1 escribirá un número entre {min} y {max}, jugador número 2 intentará adivinarlo.")
    NumJugador1 = int(getpass.getpass("Jugador número 1, introduce el número a adivinar (no se mostrará en pantalla): "))

    while NumJugador1 < min or NumJugador1 > max:
        NumJugador1 = int(getpass.getpass("Error, escribe un número dentro del rango seleccionado: "))

    while not win and chances>0:
        if len(numIntentado) == 0:
            print("Jugador 2 escribe tu primer numero: ")
        else:
            print("Estos son los numeros que has intrucido hasta el momento: " + str(numIntentado))
        NumJugador2 = int(input())  
        if NumJugador2 == NumJugador1:
            win=True
        if NumJugador2 != NumJugador1:
            chances = chances-1
            numIntentado.append(NumJugador2)
            if NumJugador2 > NumJugador1:
                print("El numero a adivinar es menor al intrucido")
            else:
                 print("El numero a adivinar es mayor al intrucido")
    if win:
        lib_adivina.win()
        name= input("Jugador 2 Escribe tu nombre porfavor: ")
        hoja2Jugadores.append([name, nivel, 1])

    else:
        lib_adivina.lose()
        print("El numero era: " + str(NumJugador1))
        name= input("Jugador 2 Escribe tu nombre porfavor: ")
        hoja2Jugadores.append([name, nivel, None])

    excelDocument.save(f"{ubicacion_archivo}\\Estadisticas.xlsx")



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
            jugarSolitario (20,1,1000)
        if opcionMenu2 == 2:
            jugarSolitario (12,1,1000)
        if opcionMenu2 == 3:
            jugarSolitario (5,1,1000)
        if opcionMenu2 == 4:
            jugarSolitarioPropioNivel()
        
    if opcionMenu1 == 2:
        menu2()
        opcionMenu2 = valida(1,5)
        if opcionMenu2 == 1:
            jugar2Jugadores (20,1,1000)
        if opcionMenu2 == 2:
            jugar2Jugadores (12,1,1000)
        if opcionMenu2 == 3:
            jugar2Jugadores (5,1,1000)
        if opcionMenu2 == 4:
            jugar2Jugadores(0, min, max, chancesPropio=True)

    if opcionMenu1 == 3:
        lib_adivina.estadistica()
        

            







     

        




