list1 = []

list2 = [1,13,4,6,7,6,4,13,5,7,4,8,9]

print(list2[0])
print(list2[4])
print(list2[-2])

# default
# start = 0
# end = len(list2) - 1
# step = 1
print(list2[:5])
print(list2[-5:])

#python - right index is not included
# left index is always included

# от третьего до восьмого включительно
print(list2[2:8])

# от восьмого до третьегов  обратном порядке
print(list2[7:1:-1])


print(list2[::-1])
