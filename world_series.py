from pprint import pprint

# A list to copy the file into
winners = []
byYear = {}
byCount = {}

# Read the file into 'winners[]' and close
with open("WorldSeriesWinners.txt", 'r') as fil:
    for i in range(1903, 2021):
        if i == 1904 or i == 1994:
            byYear[i] = 'not played'
        else:
            winner = fil.readline().rstrip()
            winners.append(winner)
            byYear[i] = winner
    fil.close()

# Go through list of winners and add the winner to byCount if its isnt already
for name in winners:
    if name not in byCount.keys():
        byCount[name] = winners.count(name)

year = int(input('Enter a year in range 1903-2020: '))



if year == 1904 or year == 1994:
    print(f'The world series wasn\'t played in the year {year}.')
elif year < 1903 or year > 2020:
    print(f'Data for the year {year} is not included in the database.')
else:
    yearWinner = byYear[year]
    numWins = byCount[yearWinner]
    print(f'The {yearWinner} won the world series in {year}.')
    print(f'They have won the World Series {numWins} times.')
