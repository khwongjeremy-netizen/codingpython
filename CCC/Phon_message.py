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
one = {'a' : 1, 'd': 1, 'g': 1, 'j': 1, 'm': 1, 'p': 1, 't': 1, 'w': 1}

#twos
two = {'b': 2, 'e': 2, 'h': 2, 'k': 2, 'n': 2, 'q': 2, 'u': 1, 'x': 2}

#threes
three = {'c': 3, 'f': 3, 'i': 3, 'l': 3, 'o': 3, 'r': 3, 'v': 3, 'y': 3}

#fours 
four = {'s': 4, 'z': 4}

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

#why is abba 12 instead of 8? a + b + pause + b + a(1+2+2+2+1)