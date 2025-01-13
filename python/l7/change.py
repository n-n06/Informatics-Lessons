li = [1,2,3,4,5]

left_index = int(input())
right_index = int(input())

li[left_index], li[right_index] = li[right_index], li[left_index]

print(li)
