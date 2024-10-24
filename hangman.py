print('lets play the hangman! give me a word', end = ' ')

word= input() 

def word_count_dict(word):
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_word_positions(letter, word):
    result = []
    position = 0
    for char in word:
        if char == letter:
            result.append(position)
        position = position + 1
    return result

word_dict = word_count_dict(word)


chances= len(word)
win=False
correct=0

print( 'your first clue is that the word has ' + str(len(word)) + ' letters \nLets start the game!' )

while not win and chances>0:
    letter= input('write the letter you would like to check: ')  
    if letter in word_dict:
        positions_list = get_word_positions(letter, word)
        correct = correct + len(positions_list)
        position = ''
        for p in positions_list:
            position = position + '#' + str(p) + ', '
        print('Yes, ' + letter + ' is part of the word and its in the ' + str(position) + ' position')
        del word_dict[letter]
    if letter not in word_dict:
        print(' this letter is not part of the word')
    if correct==len(word):
        win=True 
    chances = chances-1
if win:
    print('you won the word was: ' + word)
else:
    print('You lose! the word was:  ' + word)
     




