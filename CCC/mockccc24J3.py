'''
5
RGBAB
out: 
2
'''
integer = int(input())
word = input().lower()

start = ''
end = ''
mid = ''
r = False
g = False
b = False
for i in range(word):
    if i == 'r':
        start += i
        r = True
    if r and i == 'g':
        mid += i
        g = True
    if r and i == 'b':
        end += i
        g
    if 
    