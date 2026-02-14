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
for i in range(4):
    city = int(input('distance: '))
    cities.append(city)

for i in range(len(cities)):
    output = []
    dist = 0
    for j in range(len(cities)):
        if cities[j] != cities[i]:
            dist = abs(cities[i] - cities[j]) + dist
            output.append(dist)
        else:
            dist = 0
            output.append(dist)
    print(output)
    
