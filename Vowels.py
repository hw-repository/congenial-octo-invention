def is_vowel(x):
    vowels = {'a','e','i','o','u'}
    return x.lower() in vowels

print len('f')

while True:
    letter =raw_input('Input letter: ')

    if len(letter)==1:
        print(is_vowel(letter))
        break
    print('This is not a single letter. Please, try again...\n')
    
