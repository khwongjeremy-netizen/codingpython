'''
a
dada
bob
abba
cell
www
halt
'''
'''
1
4
7
12
13
7
'''

one = ['a', 'b', 'c']
two = ['d', 'e', 'f']
three = ['g', 'h', 'i']
four = ['j', 'k','l']
five = ['m', 'n', 'o']
six = ['p', 'q', 'r', 's']
seven = ['t', 'u', 'v']
eight = ['w', 'x' , 'y', 'z']

pause = 2
messages = []
timetotal = []
while True:
    message = input()
    if message == 'halt':
        break
    else:
        messages.append(message)

for mess in range(len(messages)):
    time = 0
    current = messages[mess]
    condition = ''
    for i in range(len(current)):
        if i+1 != len(current):
            if current[i] == current[i+1]:
                time += 2
            
            if condition == condition:
                time += 2
        if current[i]in one:
            time += 1
            condition = 'one'
        if current[i] in two:
            time += two
            condition = 'two'
        if current[i] in three: 
            time += 3
            condition = 'three'
        if current[i] in four: 
            time += 4
            condition = 'four'
        if current[i] in five: 
            time += 4
            condition = 'five'
        if current[i] in six: 
            time += 4
            condition = 'six'
        if current[i] in seven: 
            time += 4
            condition = 'seven'
        if current[i] in eight: 
            time += 4
            condition = 'eight'
        
    timetotal.append(time)

for i in timetotal:
    print(i)

#why is abba 12 instead of 8? a + pause +  b + pause + b + pause + a(1+2+2+2+2+2+1)
