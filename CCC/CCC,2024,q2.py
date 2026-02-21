Dusa = int(input())
yobi = []
size = Dusa
while True:
    yobi_size = input()
    if yobi_size == '':
        break
    else:
        yobi.append(int(yobi_size))

for i in range(len(yobi)):
    if yobi[i] < size:
        size += yobi[i]
        print('added')

print(size)