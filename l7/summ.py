import random
array = [random.randint(0, 100) for i in range(random.randint(5,15))]

print(array)
summ = 0

for i in range(len(array)):
    if array[i] % 2 == 0 and i % 2 != 0:
        summ += array[i]

print(summ)
