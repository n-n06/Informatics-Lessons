import array as arr
from random import randint

my_array = arr.array('i', [randint(0,100) for x in range(randint(5,10))])
print(my_array)
li1 = [1,2,3]
print(li1)



for array_element in my_array:
    print(array_element, end = " ")
    array_element += 1
    print(array_element)
    
print(my_array)


print(len(my_array))

# arr, li
# [1,2,3,4,5]
#  0 1 2 3 4

for i in range(len(my_array)): # 0,1,2,3,4
    print(my_array[i], end= " ")
    my_array[i] += 1
    print(my_array[i])

print(my_array)
    
