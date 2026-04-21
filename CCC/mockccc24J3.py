'''
5
RGBAB
out: 
2
'''
integer = int(input())
word = input().lower()


total = 0
for i in range(word):
    first = i
    second = i+1
    third = i+3
    if word[first] == 'r' and word[second] == 'g' and word[third] == 'b':
        total += 1
print(total)