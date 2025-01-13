import array as arr

a = arr.array('i', [1,2,3,4,5,6,7])
element = int(input()) # 55   
index = int(input()) # 6 --> 5

a.insert(index - 1, element)
print(a)
