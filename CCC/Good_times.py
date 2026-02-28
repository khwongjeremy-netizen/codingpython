input_time = int(input())

zones = ['Ottawa', 'Victoria', 'Edmonton', 'Winnipeg', 'Toronto', 'Halifax', "St. John's"]
st_johns = 0
times = []
for i in range(len(zones)):
    time = 0
    if zones[i] == zones[0]:
        time += input_time
    if zones[i] == zones[1]:
        time += input_time - 300
    if zones[i] == zones[2]:
        time += input_time- 200
    if zones[i] == zones[3]:
        time += input_time- 100
    if zones[i] == zones[4]:
        time += input_time
    if zones[i] == zones[5]:
        time += input_time + 100
    if zones[i] == zones[6]:
        time += input_time + 130
    if time < 2400:
        times.append(time)
    else:
        time -= 2400 
        times.append(time)

for i in range(len(times)):
    print(str(times[i]) + ' in {}'.format(zones[i]))
#3 wrong