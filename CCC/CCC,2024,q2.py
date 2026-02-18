Dusa = int(input())
yobi = []
size = 0
while True:
    yobi_size = int(input())
    if yobi_size == '':
        break
    yobi.append(int(yobi_size))

for i in range(len(yobi)):
    if yobi[i] > size:
        size += yobi[i]

print(size)