a = int(input())
b = int(input())

for i in range(a, b + 1):
    #a = 1, b = 5,      i = 1,2,3,4,5
    if i % 2 == 0:
        continue
    
    print(i)
