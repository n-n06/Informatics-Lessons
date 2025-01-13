file = open('oddnumbers.txt', 'w')

n = int(input())

li = []
for i in range(n):
    num = int(input())
    if num % 2 != 0:
        file.write(str(num) + ' ')
    li.append(num)


file.close()
