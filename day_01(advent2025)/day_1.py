x = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
'''

import re
mid = 50
matches = re.findall(r'([a-zA-Z])(\d+)', x)
result = [(char, int(num)) for char, num in matches]
'''
I plan to change the entire combination order into a list of tuples and then I will analyze the tuples to generate the password'''
num = 0 
for i in range(len(result)):
    turn = result[i][1]
    direction = result[i][0]
    if direction == 'R':
        mid += turn
        while mid > 100:
            num += 1
        mid -= 100
    elif direction == 'L':
        mid -= turn
        while mid < 0:
            num += 1
            mid += 100
    if mid == 0 or mid == 100:
        num += 1
    print(mid)
print(num)