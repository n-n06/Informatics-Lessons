import array as arr

a = arr.array('i', [4,5,6,22,6,7,13,9])

avg = sum(a) / len(a)
print(avg)

i = 0
while i < len(a):
    if a[i] > avg:
        a.pop(i)
    else:
        i = i + 1




print(a)
