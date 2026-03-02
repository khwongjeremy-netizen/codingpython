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
#ones 
one = ['a', 'd', 'g', 'j', 'm', 'p', 't', 'w']

#twos
two = ['b','e', 'h','k','n', 'q', 'u', 'x']

#threes
three = ['c', 'f', 'i', 'l', 'o', 'r', 'v', 'y']

#fours 
four = ['s', 'z']

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
    for i in range(len(current)):
        if i+1 != len(current):
            if current[i] == current[i+1]:
                time += 2
            if 
        if current[i]in one:
            time += 1
        if current[i] in two:
            time += 2
        if current[i] in three: 
            time += 3
        if current[i] in four: 
            time += 4
        
    timetotal.append(time)

for i in timetotal:
    print(i)

#why is abba 12 instead of 8? a + pause +  b + pause + b + pause + a(1+2+2+2+2+2+1)