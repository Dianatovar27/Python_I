
varI= input()
varII= input()
varIII= input()

print(int(varI)>100 or int(varII)>100 or int(varIII)>100)


Valor1= 5
Valor2= 'start'


print('Whats your name?', end='')
name= input()
print('good morning,', name)

var1= int(input())

if var1 > 0:
    print('its positive')
else:
    print('its 0 or not positive')



num1= int(input())
num2= int(input())
num3= int(input())

if (num1 > num2) and (num1> num3):
    print( 'the biguest number is: ', num1)
elif (num2 > num1) and (num2 > num3):
    print( 'the biguest number is: ', num2)
else:
    print('the biguest number is: ', num3)




print('give me a number', end ='')

number= int(input())

while not (number> 1000 and number<1500):
    print('try another number')
    number= int(input())
else:
    print('tha number its in between 1000 and 1500')




print('give me a number between 1 and 10', end =' ')
number1= int(input())

for n in range(11):
    print(n * number1)



print(' give 2 numbers:', end= ' ')
n1=int(input())
n2=int(input())

print('select one option:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide')
option=int(input())

if option == 1:
    print(n1 + n2)
if option == 2:
    print(n1 - n2)
if option == 3:
    print(n1 * n2)
if option == 3:
    print(n1 / n2)


print ('give me a number between 1 - 10', end= ' ' )

x= int(input())

if x >= 1 and x <= 4:
    print ('suspense' )
if x >= 5 and x <= 6:
    print ('good' )
if x >= 7 and x <= 8:
    print ('notable' )
if x >= 9 and x <= 10:
    print ('outstanding' )