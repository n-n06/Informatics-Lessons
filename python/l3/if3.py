a = int(input())
b = int(input())
c = int(input())

min = max = a

if a >= b and a >= c:
    max = a
    if b >= c:
        min = c
    else:
        min = b
elif b >= a and b >= c:
    max = b
    if a >= c:
        min = c
    else:
        min = a
else:
    max = c
    if a >= b:
        min = b
    else:
        min = a

print("Average: ", (a + b + c) / 3)
print((max / min) * 100, "%")

