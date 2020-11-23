fil = open('steps.txt', 'r', encoding='utf-8')
stepList = fil.readlines()
fil.close()

months = {
    'Jan': [31],
    'Feb': [28],
    'Mch': [31], 
    'Apr': [30], 
    'May': [31],
    'Jun': [30],
    'Jul': [31],
    'Aug': [31],
    'Sep': [30],
    'Oct': [31],
    'Nov': [30],
    'Dec': [31]
}

counter = 0

print('The number of steps taken each month were: ')
for month in months.keys():
    days = months[month][0]
    monTot = 0
    
    for i in range(counter, counter+days):
        steps = int(stepList[i])
        monTot += steps
        counter += 1
    
    avg = round(monTot/days, 1)
    print(f'{month}\t: {avg}')

