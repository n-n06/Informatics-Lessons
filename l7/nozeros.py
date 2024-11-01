n = int(input())
li = list(map(int, input().split()))

count = 0

for i in range(len(li)):
    if li[i] == 0:
        count += 1
        li[i] = i
print(li)
print("Количество замененных чисел =", count)
