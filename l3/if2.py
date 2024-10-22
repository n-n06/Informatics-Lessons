import math

if 4 > 3 > 5:
    print("wow")

n = int(input())

'''
sqrt = square root = кв корень


16
math.sqrt(16) = 4.0

4.0 == int(4.0) = 4
4.0 == 4 = True => perfect 

18
math.sqrt(18) = 4.23939
4.23939 == int(4.23939)
int(4.23939) = 4
4.23939 == 4 = False => imperfect
'''


if (math.sqrt(n) == int(math.sqrt(n))):
    print("perfect")
else:
    print("not perfect")
