days = int(input())
weather = []
'''
8
P
S
P
S
S
P
P
S
'''
sunny_day = 0
max_days = 0
for i in range(days):
    weather_day = input()
    weather.append(weather_day)
print(weather)

for i in range(len(weather)):
    weather[i] == 's'
    for j in range(len(weather)):
        if weather[j] == 's':
            sunny_day += 1
        elif sunny_day > max_days:
            max_days = sunny_day

        print(sunny_day)
        sunny_day = 0
print(max_days)