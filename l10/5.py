








n = int(input())
li = []
for i in range(n):
    a = int(input())
    li.append(a)


for i in range(n // 2):
    print(li[i] + li[-i-1])

if n % 2 != 0:
    print(li[n // 2])
