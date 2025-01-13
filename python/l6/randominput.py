import random

n = int(input())

li = [0] * n

for i in range(n):
    li[i] = random.randint(0, 100)

print(li)
