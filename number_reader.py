fil = open('random_numbers.txt', 'r')
nums = fil.readlines()
numsRead = len(nums)
high = 0
low = 500
total = 0
for num in nums:
    num = int(num)
    if num > high:
        high = num
    if num < low:
        low = num
    total += num

avg = total/numsRead

print(f'{numsRead} numbers were read from the file.')
print(f'Max: {high}')
print(f'Min: {low}')
print(f'Sum: {total}')
print(f'Avg: {avg}')
