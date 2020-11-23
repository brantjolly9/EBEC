# A program to determine statistics about a given number list
nums = [1.5, 6, 9.2, 1.35, 3.14, 3.1415, 2.3, 18, 2.33, 2.718]
# Variables to store stats
high = 0
low = 100
total = 0

for i in range(1, 11):
    print('Enter number\t', end= '')
    num = float(input(f'{i} of 10: '))
    nums.append(num)
    total += num

    # Test for list stats
    if num > high:
        high = num
    if num < low:
        low = num

avg = '{:.2f}'.format(total/len(nums))
total = '{:.2f}'.format(total)
low = '{:.2f}'.format(num)
high = '{:.2f}'.format(num)
print(f'Lowest number: {low}')
print(f'Highest number: {high}')
print(f'Total: {total}')
print(f'Average: {avg}')
