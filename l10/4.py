







n = int(input())

for i in range(n):
    for space in range(n - 1 - i):
        print(" ", end = "")
    
    for j in range(2 * i + 1):
        print("*", end = "")

    print()