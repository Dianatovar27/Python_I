print('lets play the hangman! give me a word', end = ' ')

word= input() 
list_word = list(word)
chances= len(list_word)
win=False
correct=0

print( 'your first clue is that the word has ' + str(len(list_word)) + ' letters \nLets start the game!' )

while not win and chances>0:
    letter= input('write the letter you would like to check: ')
    attempt = 0
    #for w in list_word:    
    if letter in list_word:
            attempt = attempt + 1
            position = list_word.index(letter)
            correct = correct + 1
            print('Yes, ' + letter + ' is part of the word and its in the #' + str(position) + ' position')
    if letter not in list_word:
            attempt = attempt + 1
            print(' this letter is not part of the word')
    if correct==len(list_word ):
     win=True 
    chances = chances-1
if win:
    print('you won the word was: ' + word)
else:
    print('You lose the word was:  ' + word)
     




