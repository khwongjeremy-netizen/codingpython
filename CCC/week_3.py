play = ['A', 'B', 'C', 'D', 'E']
while True:
    b = int(input('B: '))
    n = int(input('N: '))
    if b == 1:
        for i in range(n):
            play = play[1:] + [play[0]]
            print(play)
    elif b == 2:
        for i in range(n):
            play = [play[-1]] + play[:-1]
            print(play)
    elif b == 3:
        for i in range(n):
            play[1], play[0] = play[0], play[1]
            print(play)
    elif b == 4: 
        print(play)
        break