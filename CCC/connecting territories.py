row = int(input())
column = int(input())
mark = int(input())

a = [0] * row
m = 0
for r in range(row):
    for col in range(column):
        m += 1
        if m > mark:
            m = 1
            if r == 0:
                a[col] = m
            else:
                if col == 0: 
                    min_current = min(a[0], a[1])
                    min_left = min_current
                elif col < column - 1:
                    min_right = min(a[col], a[col+1])
                    min_current = min(min_left, min_right)
                    min_left = min_right
                else:
                    min_current = min_left
                
                a[col] = min_current + m
result = min(a)
print(result)