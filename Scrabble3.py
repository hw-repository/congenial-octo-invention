import random

SCRABBLE_LETTER_VALUES = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1,
                           'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8,
                           'y':4,'z':10}
HAND_SIZE = 10


def read_words(filename='20k.txt'):
    ''' Read file of most popular english words'''
    with open(filename) as words_file:
        words = words_file.read()
    words = [word for word in words.split('\n') if len(word) > 1]
    return words

def dealHand(hand_size):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    hand = ''
    for i in range(hand_size):
        hand+= random.choice(letters)
    return hand


def getFrequencyDict(word):
    frequencyDict = dict()
    for i in range (len(word)):
        value = frequencyDict.get(word[i],0)
        value+=1
        frequencyDict.update({word[i]:value})
    return frequencyDict
        
        
def displayHand(hand):
    frequencyDict = getFrequencyDict(hand)
    hand_formatted =''
    for key in frequencyDict:
        for i in range(frequencyDict[key]):
            hand_formatted+=key
    return hand_formatted
    

def recalculateHand(hand,word):
    word_dict = getFrequencyDict(word)
    hand_dict = getFrequencyDict(hand)
    hand = ''
    for key in word_dict:
        hand_dict[key]=hand_dict[key] - word_dict[key]
    for key in hand_dict:
        for i in range(hand_dict[key]):
            hand+=key
    return hand
  
    
        

def isValidWord(word,hand):
    
    words = read_words()
    inWords = word in words
    inHand = True
    word_dict = getFrequencyDict(word)
    hand_dict = getFrequencyDict(hand)
    for key in word_dict:
        dif = hand_dict.get(key,0)-word_dict.get(key,0)
        if(dif<0):
            inHand = False
            break
    return (inHand and inWords)


            
def get_word_score(word,n):
    score = 0
    word_length = len(word)
    for i in range(word_length):
        score+= SCRABBLE_LETTER_VALUES.get(word[i],0)
    score*=word_length
    if (word_length==n):
        score+=50
    return score



def compPlayHand(hand,n):
    hand_dict = getFrequencyDict(hand)
    words = read_words()
    prevScore = 0
    biggestScore = 0
    bestWord = ''
    for i in range (len(words)):
        current = words[i]
        current_dict = getFrequencyDict(current)
        inHand = True        
        for key in current_dict:
            dif = hand_dict.get(key,0)-current_dict.get(key,0)
            if(dif<0):
                inHand = False
                break
        if(inHand == True):          
            score = get_word_score(current,n)
            '''print('Current "{0}" earned  {1} points.'.format(current,score))'''
            if(score>biggestScore):
                bestWord = current
                biggestScore = score                
    print('Best "{0}" earned  {1} points.'.format(bestWord,biggestScore))            
    return bestWord


def userPlayHand(hand,n):
    totalScore = 0
    while True: 
        choice3 = raw_input('Enter word, or a "." to indicate that you are finished:')
        if(choice3=='.'):
            break
        
        word = choice3
        if (isValidWord(word,hand)):
            score = get_word_score(word.lower(),n)
            totalScore+=score
            print('"{0}" earned  {1} points. Total: {2}'.format(word,score,totalScore))
            hand = recalculateHand(hand,word)
            if(hand==''):
                print('Run out of letters. Total score: {0} points.'.format(totalScore))
                break
        else:
            print('Invalid word, please try again.')
    print('\n')


def playGame(hand,n):
    print('Current hand: {0}'.format(displayHand(hand)))
    while True:        
        player_choice = raw_input('Enter u to have yourself play, c to have the computer play:')
        if(player_choice == 'u'):
            userPlayHand(hand,n)
            break
        elif(player_choice == 'c'):
            compPlayHand(hand,n)
            break
        print('Invalid command.')
        
            
    
lastHand = dealHand(HAND_SIZE)

while True:
    
    choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
    if(choice=='n'):
        hand = dealHand(HAND_SIZE)
        lastHand = hand
        playGame(hand,HAND_SIZE)
    elif(choice=='r'):
        hand = lastHand
        playGame(hand,HAND_SIZE)
    elif(choice=='e'):
        break
    else:
        print('Invalid command.')
        hand = lastHand
        
    

            
        
    
    

