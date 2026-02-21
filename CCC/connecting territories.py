length = input()
width = input()
division = int(input())
grid = int(length)*int(width) 
layout = []
index = 0
for i in range(grid):
    index += 1
    if index <= division:
        layout.append(index)
    else: 
        index = 1

print(layout)
for i in range(layout):

    
