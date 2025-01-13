import math


point1 = (4,5)
point2 = (1,1)

dist = math.sqrt(
    (point2[0] - point1[0]) ** 2 +
    (point2[1] - point1[1]) ** 2
    )
print(dist)


with open('output.txt', 'a') as file:
    file.write(str(dist))

print()


