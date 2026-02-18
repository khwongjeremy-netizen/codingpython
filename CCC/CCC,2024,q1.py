#sushi
red = 3
green = 4
blue = 5
total = 0
red_num = int(input())
blue_num = int(input())
green_num = int(input())
if red_num > 0:
    total += red_num * red
if green_num > 0:
    total += green_num * green
if blue_num > 0:
    total += blue_num * blue

print(total)
