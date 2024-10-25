import random2
import openpyxl

excel_document= openpyxl.load_workbook("C:\\Users\\jfdr1\\Desktop\\Python_I\\Estadisticas.xlsx")

hoja = excel_document["Jugadores"]

def menu():
    print("Selecciona una opcion: ")
    print("1. Partida modo solitario")
    print("2. Partida 2 Jugadores")
    print("3. Estadística")
    print("4. Salir")

def valida(min, max):
    if min > max:
        print("error min can't be bigger than max")
    opcion = int(input("Escribe una opción: "))
    while opcion < min or opcion > max:
        opcion = int(input("Error, escribe una opción entre 1 y 4: "))
    return opcion

def menu2():
    print("Selecciona un nivel: ")
    print("1. Fácil (20 intentos)")
    print("2. Medio (12 intentos)")
    print("3. Difícil (5 intentos)")
    print("4. Regresar al menu principal")

while True:
    opcion = 0
    menu()
    opcion = valida(1, 4)

    if opcion == 4:
        break

    if opcion == 1:
        menu2()
        opcion = valida(1, 4)
        if opcion == 1:
            chances= 20
            win=False
            numIntentado = []
            #correct=0
            soliNumRandom=random2.giveMeNumber(1,1000)
            print("Adivina un numero del 1 al 1000, recuerda que tienes solo 20 intentos: ")
            while not win and chances>0:
                if len(numIntentado) == 0:
                    print(" escribe tu primer numero")
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
                print("ADIVINASTE! FELICIDADES!!")
                name= input("Escribe tu nombre porfavor: ")
                hoja.append([name, 1])
                excel_document.save("C:\\Users\\jfdr1\\Desktop\\Python_I\\Estadisticas.xlsx")
            else:
                print("Perdiste el numero era: " + str(soliNumRandom))
                name= input("Escribe tu nombre porfavor: ")
                hoja.append([name, None, 1])
                excel_document.save("C:\\Users\\jfdr1\\Desktop\\Python_I\\Estadisticas.xlsx")


    

     

        




