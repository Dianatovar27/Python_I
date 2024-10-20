print( 'How many words would you like to add to your list (minimum 7)?', end = ' ')
listnumber = int(input())
list=[]
print('Plese give me ', listnumber, ' words:')

for w in range(listnumber):
    w= input()
    list.append (w)
print(list)