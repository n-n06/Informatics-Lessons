import math
number = int(input())

# простое - делится только на себя и на единиице
flag = True

for i in range(2, int(math.sqrt(number))):
    #2 - number не включительно
    if number % i == 0:
        flag = False
        break

print(flag)
