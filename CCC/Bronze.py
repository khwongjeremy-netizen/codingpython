
num = int(input())
contest = []
for i in range(num):
    score = int(input())
    contest.append(score)
omits = []
for j in range(3):
    best = 0
    for i in range(len(contest)):
        if contest[i] > best and contest[i] not in omits:
            best = contest[i]
    omits.append(best)

print(omits)
bronze = omits[2]
amt = 0
for i in contest:
    if i == bronze:
        amt += 1
print(str(bronze) + " " + str(amt))

#Why is it wrong???