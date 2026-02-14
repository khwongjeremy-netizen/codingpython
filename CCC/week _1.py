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
dist = 0
yeah = []
for i in range(4):
    city = int(input('distance: '))
    cities.append(city)
for j in range(len(cities)):
    dist = abs(cities[0] - cities[j]) + dist
    output.append(dist)
for i in range(len(output)):
    yeah = []
    for j in range(len(output)):
        out = abs(output[i] - output[j])
        yeah.append(out)
    print(yeah)

    
