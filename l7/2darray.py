n = int(input())
m = int(input())

matrix = []

for i in range(n):
    matrix.append([0]*m)
    for j in range(m):
        matrix[i][j] = int(input())

print(matrix)
print(sorted(matrix))
matrix2 = [[1,2,3], [4,5]]

print(matrix2)
