# A program to run a simulation of a million roles of a dice
from random import randint

results = []
for i in range(1000000):
    roll = randint(2, 12)
    results.append(roll)

two = '{:.2f}'.format(results.count(2)/len(results)*100)
thr = '{:.2f}'.format(results.count(3)/len(results)*100)
fur = '{:.2f}'.format(results.count(4)/len(results)*100)
fiv = '{:.2f}'.format(results.count(5)/len(results)*100)
six = '{:.2f}'.format(results.count(6)/len(results)*100)
sev = '{:.2f}'.format(results.count(7)/len(results)*100)
eit = '{:.2f}'.format(results.count(8)/len(results)*100)
nin = '{:.2f}'.format(results.count(9)/len(results)*100)
ten = '{:.2f}'.format(results.count(10)/len(results)*100)
ele = '{:.2f}'.format(results.count(11)/len(results)*100)
twl = '{:.2f}'.format(results.count(12)/len(results)*100)
print('Roll:  Frequency')
print(f'2:  {two}')
print(f'3:  {thr}')
print(f'4:  {fur}')
print(f'5:  {fiv}')
print(f'6:  {six}')
print(f'7:  {sev}')
print(f'8:  {eit}')
print(f'9:  {nin}')
print(f'10:  {ten}')
print(f'11:  {ele}')
print(f'12:  {twl}')
