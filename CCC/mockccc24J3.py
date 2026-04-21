'''
5
RGBAB
out: 
2
'''
integer = int(input())
word = input().upper()
start = False
mid = False
total = 0
for i in range(integer):
    if word[i] == 'R':
        start = True
        for j in range(integer-i):
            if word[j] == 'G':
                mid = True
            if word[j] == 'B':
                if start and mid:
                    total += 1
                mid = False
                start = False
                break 
                
print(total)