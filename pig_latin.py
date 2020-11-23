# Pig latin converter
sentence = 'Coding is fun'


sentence = str(input('Enter a string: '))
words = sentence.split(' ')

for word in words:
    letter = word[0]
    print(word.lstrip(letter) + letter + 'ay ', end='')


    




