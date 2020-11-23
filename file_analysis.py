from pprint import pprint
import re

# Open the two files, read them into lists, close the files
xian1 = open('xian_1.txt', 'r')
xian2 = open('xian_2.txt', 'r')
xi = xian1.read()
jingping = xian2.read()
xian1.close()
xian2.close()

# Function to cut the paragraph into words
def cutter(paragraph):
    cutParagraph = []

    # Split each sentence to avoid problems I encounted when writing this part
    sentences = paragraph.split('.')
    for sentence in sentences:
        words = sentence.split(' ')
        for word in words:
            word = word.lower()                 # Make word lowercase and strip whitespace
            word = word.strip()
            
            # Remove any characters not letters
            if not word.isalpha():
                for char in word:
                    if not char.isalpha():
                        word = word.replace(char, '')
                cutParagraph.append(word)

            else:
                cutParagraph.append(word)
    
    # Final cleanup for blanks
    for word in cutParagraph:
        if word == '':
            cutParagraph.remove(word)

    return cutParagraph


words1 = cutter(xi)
words2 = cutter(jingping)

# Determine the freqency with which certain words appear
def frequency(words):

    # Dict to keep track of words and frequency
    freq = {}

    for word in words:
        if word not in freq.keys():                 # Check is word has been seen before
            freq[word] = words.count(word)
    return freq

def common(words1, words2):
    comList = []
    for word in words1:
        if word in words2 and word not in comList:
            comList.append(word)
    return comList


def different(words1, words2):
    diff = []
    
    for word in words1:
        if word not in words2 and word not in diff:
            diff.append(word)
    
    for word in words2:
        if word not in words1 and word not in diff:
            diff.append(word)
    
    
    diff.sort()
    return diff

diff1 = different(words1, words2)
print(diff1)
