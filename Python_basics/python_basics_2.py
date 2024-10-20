#print( 'How many words would you like to add to your list (minimum 7)?', end = ' ')
#listnumber = int(input())
#list=[]
#print('Plese give me', listnumber, 'words: ')

#for w in range(listnumber):
    #w= input()
    #list.append (w)
#print(list)

# Se pide un numero entre 1 y 7, más una palabra. El numero introducido indica la posición en la lista anterior cuyo valor será sustituido por la palabra introducida.

#numb = int(input('give me a number between 1 and 7: '))
#nw= input('give me a new word: ')

#list[numb] = nw
#print(list)

# Se pide la posición de un elemento en la lista y una vez introducida se elimina dicha palabra.

#delete= int(input( 'which position betweeen 1 and 7 would you like to delete? '))

#del list[delete]

# Crea un diccionario de 10 palabras ingles-español y realiza 3 consultas a este diccionario

#dictranslate= {'dog': 'perro', 'cat': 'gato', 'table' : 'mesa', 'car': 'carro', 'girl' : 'nina', 'boy' : 'nino', 'sun' : 'sol', 'moon':'luna', 'pencil': 'lapiz', 'flower': 'flor' }

#for i in range(3):
    #ingles= input('which word would you like to check? ')
    #print(dictranslate[ingles])

#dictranslate.update({'house': 'casa'})

#print(dictranslate)

# Introduce una lista de 10 palabras y muéstralas de la ultima a la primera

#nlist=[]

#for i in range(10):
    #nlist.append(input())
#print(nlist)

#contador = 9
#for w in range(10):
    #print(nlist[contador])
    #contador = contador-1

# Mediante funciones realiza un programa que simule una calculadora


def menu():
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    

def check():
    if option < 1 or option > 4:
        print('pick an option between 1 and 4')
        return False
    return True

def add(val1, val2):
    return val1 + val2

def sub(val1, val2):
    return val1 - val2

def mul(val1, val2):
    return val1 * val2

def div(val1, val2):
    return val1 / val2

     
menu()
option = int(input('Pick a number: '))
while not check():
    menu()
    option = int(input('Pick a number: '))

val1= int(input('enter first value: '))
val2= int(input('enter second value: '))

if option == 1:
    print( add(val1, val2))

if option == 2:
    print( sub(val1, val2))

if option == 3:
    print( mul(val1, val2))

if option == 4:
    print( div(val1, val2))