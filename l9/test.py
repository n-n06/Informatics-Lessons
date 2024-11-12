def double_list():
    global li
    for i in range(len(li)):
        li[i] = 2 * li[i]

li = [1,2,3]
print(li)
print(double_list())
print(li)
