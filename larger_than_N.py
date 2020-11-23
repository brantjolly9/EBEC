# Program to determine which numbers in a list are greater than a given number
numList = [19, 2940, 10, 24, 29, 1, 85, 201, -15, -122, 799]
subList = []

number = float(input('Number: '))
print(f'List of numbers:\n{numList}')

for num in numList:
    if number < num:
        subList.append(num)
print(f'Numbers in list that are larger than 13:\n{subList}')
