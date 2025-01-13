a = int(input())
b = int(input())
l = int(input())
n = int(input())


a_len = a * ((n - 1) * 2 + 1)
b_len = (n - 1) * b * 2
l_len = l * 2

print(a_len + b_len + l_len)
