# import array as arr
#  я xочу из аррай полчуить только непосредственный класс массива
from array import array 

# imports
# 1. import module
# 2. import module as m
# 3. from module import class



a = array('i') #i = int = integer = целое число
a.append(5)
a.append(4)

for element in a:
    print(element ** 2)


# склад - коробками
# точно знаю в какой коробке какого типа товары находятся
# быстрее разносить быстрее переносить быстрее считать

#array module - array class


print(a)
