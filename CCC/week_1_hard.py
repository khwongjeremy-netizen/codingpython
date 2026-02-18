# Ri = {Ri,1...,R,li}
first_input = input()
recommend = int(first_input[0])
restaurant = int(first_input[1])
array = {}
R_value = 0
recomends =[]
for i in range(restaurant):
    for j in range(recommend):
        recomends.append('R{}'.format(j))
        array['R{}'.format(i+1)] = recomends
        recomends = [] 
print(array)
