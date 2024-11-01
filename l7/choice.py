k = int(input())
li = list(map(int, input().split()))

chosen_ones = []

for i in range(len(li)):
    if li[i] == 5:
        chosen_ones.append(i)

print(chosen_ones)

