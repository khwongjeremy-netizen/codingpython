#Modulus thing
a, b = int(input('A: ')), int(input('B: '))

n = 0
while True:
    d = a * n
    if d % b == 1:
        print(n)
    elif n < b:
        n += 1
    else:
        print("No such integer exists")