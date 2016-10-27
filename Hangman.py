import random

def read_words(filename='20k.txt'):
    ''' Read file of most popular english words'''
    with open(filename) as words_file:
        words = words_file.read()
    words = [word for word in words.split('\n') if len(word) > 5]
    return words


def choose_random_word(words):
    ''' Choose random word from list '''
    return random.choice(words)

def print_word(guess_set,word):
    out_str = ''
    for j in range(len(word)):
        if (word[j] in guess_set):
            out_str+= word[j]
        else:
            out_str+='_'
    return out_str
            

word = choose_random_word(read_words())
wordList = word.split()
wordSet = set({})
guess_set = set({})

for i in range(len(word)):
    wordSet.add(word[i])

    
#print(wordSet)

print('Welcome to the game, Hangman!')
print ('You have {0} guesses left'.format(len(word)))

for i in range(len(word)):
    print('Available letters: abcdefghijklmnopqrstuvwxyz')
    letter = str(raw_input('Please guess a letter: '))
    guess_set.add(letter)
    if (letter in wordSet):
        print('Good guess: %s' %print_word(guess_set,word))
    else:
        print('Oops! That letter is not in my word: %s' %print_word(guess_set,word))
    if(guess_set==wordSet):
        print('Congratulations!')
        break

if (guess_set!=wordSet):
    print('Sorry, but you lost.')
    print('The word I am thinking: %s'%word)
    

