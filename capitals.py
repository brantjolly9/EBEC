from pprint import pprint
caps = open('state_capitals.txt', 'r')
stateCaps = {}

for i in range(10):
    pair = caps.readline()
 
    duo = pair.split(', ')
    stateCaps[duo[0]] = duo[1].rstrip()

# for pair in caps.readlines():
#     duo = pair.split(', ')
#     duo[1].replace("\n", "")
#     print(duo[1])
    
#     stateCaps[duo[0]] = duo[1]


pprint(stateCaps, indent=2)
caps.close()
