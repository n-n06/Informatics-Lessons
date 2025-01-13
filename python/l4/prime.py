# 2 3 5 7 11 13 17 19 23 29 31 37 ....

n = int(input())
# n = 14

#else break
for i in range(2, n):
    #i = 2,3,4,5,6,7,8,9,10,11,12
    if n % i == 0:
        print("непростое")
        break
else:
    print("простое")



