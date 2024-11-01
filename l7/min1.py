n= int(input())

li = [0]*n
for i in range(n):
    li[i] = int(input())

min_x = max_x = li[0]

for i in range(n):
    if li[i] < min_x:
        min_x = li[i]
    if li[i] > max_x:
        max_x = li[i]

print("min: ", min_x, ", max: ", max_x)
        


import random
array = [random.randint(0, 100) for i in range(random.randint(5,15))]
         
