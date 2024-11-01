n = int(input())
m = int(input())

matrix = []

for i in range(n):
    matrix.append([])
    matrix[i] = list(map(int, input().split()))

max = matrix[0][0]
for i in range(n):
    for j in range(m):
        if matrix[i][j] > max:
            max = matrix[i][j]

print(max)

