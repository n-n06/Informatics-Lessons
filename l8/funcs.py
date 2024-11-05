def give_one():
    return 1

print(give_one())

def sum(a, b):
    global c
    c = a + b
    return c

print(sum(4,5))
print(c)

