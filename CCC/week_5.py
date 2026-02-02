people = int(input('number of people: '))
candidates = []
bids = []
highest = 0
for i in range(people):
    name = input('Name: ')
    bid = int(input('Bid: '))
    candidates.append(name)
    bids.append(bid)

for i in range(people):
    if bids[i] > highest:
        highest = bids[i]
        winner = candidates[i]
print(winner)
    
