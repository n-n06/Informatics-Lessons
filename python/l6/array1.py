import array as arr

a = arr.array('i')

num_array1 = arr.array('i', [1,2,3,4])
print(num_array1)



num_array2 = arr.array('i')

for i in range(5):
    element = int(input("INput a number: "))
    num_array2.append(element) 

print(num_array2)
