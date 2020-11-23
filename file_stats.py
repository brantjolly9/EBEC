# Program to get the statistics of a story

# Create list so I can close the file
rump = []
with open('RUMPELSTILTSKIN.txt', 'r', encoding='utf-8') as r:

    # Given line limit
    for i in range(72):
        line = r.readline().strip()
        rump.append(line)
    r.close()

wordCount = 0
for line in rump:

    # Seperates the words by spaces
    words = line.split(' ')
    for word in words:

        # Ignore the blanklines
        if word != '':
            wordCount += 1
print(f'Total number of words: {wordCount}')
print(f'Total number of lines: {len(rump)}')
print(f'Average number of words per line: {round(wordCount/len(rump), 1)}')





