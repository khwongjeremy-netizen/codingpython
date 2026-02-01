while True:
    b = int(input('B: '))
    n = int(input('N: '))
    play = ['A', 'B', 'C', 'D', 'E']
    if b == 1:
        for i in range(n):
            play = [play[:3]] + [play[0]]
    elif b == 2:
        for i in range(n):
            play = [play[4]] + [play[:3]]
    elif b == 3:
        for i in range(n):
            play[1], play[0] = play[0], play[1]
    elif b == 4: 
        print(play)
        break