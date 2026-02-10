#Modulus thing
a, b = int(input('A: ')), int(input('B: '))

n = 0
while True:
    d = a * n
    if d % b == 1:
        print(n)
        break
    elif n < b:
        n += 1
    else:
        print("No such integer exists")
        break

    '''
input:
3 10 12 5

output:
0 3 13 25 30
3 0 10 22 27
13 10 0 12 17
25 22 12 0 5
30 27 17 5 0
'''
cities = [0,]
output = []
for i in range(4):
    city = int(input('distance: '))
    cities.append(city)

for i in range(len(cities)):
    output = []
    for j in range(len(cities)):
        dist = abs(cities[i] - cities[j])
        output.append(dist)
    print(output)
