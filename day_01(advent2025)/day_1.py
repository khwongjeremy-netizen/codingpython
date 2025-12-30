import re
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
max = 99
min = 0
mid = 50
matches = re.findall(r'([a-zA-Z])(\d+)', x)
result = [(char, int(num)) for char, num in matches]
num = 0 
for i in range(len(result)):
    atzero = True
    turn = result[i][1]
    direction = result[i][0]
    if direction == 'L':
        if mid == 0:
            atzero = False
        mid -= turn
        while mid < 0:
            if atzero:
                num += 1
            mid += 100
    elif direction == 'R':
        if mid == 100:
            atzero = False
        mid += turn
        while mid > 100:
            if atzero: 
                num += 1
            mid -= 100
    if mid == 0 or mid == 100:
        num += 1
    print(mid)
print(num)