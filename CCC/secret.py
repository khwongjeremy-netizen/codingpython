
'''
57234
00907
34100
99999

right 234
right 907
left 100
'''

directions = []
while True: 
    inp = input()
    if inp == '99999':
        break
    directions.append(inp)

for i in range(len(directions)):
    first = int(directions[i][0])
    second = int(directions[i][1])
    answer = first + second 
    if answer % 2 == 0:
        vector = "right "
    else: 
        vector = "left "
    print(vector + str(directions[i][2:]))