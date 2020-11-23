keypad = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}

num = input('Enter a telephone number: ')

sections = num.split('-')

def convert(word, keypad):
    word = word.lower()
    num = []
    for letter in word:
        
        for butn in keypad.items():
            if letter in butn[1]: 
                num.append(str(butn[0]))
    number = ''.join(num)
    return number

final = sections[0] + '-' + convert(sections[1], keypad) + '-' + convert(sections[2], keypad)
print(f'The phone number is {final}')

  
        

