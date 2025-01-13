a = int(input())
b = int(input())
c = int(input())


if a <= b and a <= c:
    print("a is min: ", a)
else:
    if b <= a and b <= c:
        print("b is min: ", b)
    elif c <= a and c <= b:
        print("c is min: ", c)


