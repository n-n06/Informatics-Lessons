import random

number_list = []

for i in range(20):
    number = random.randint(-100, 100)
    number_list.append(number)

print(number_list)


'''
1. пройтисб глазами по всему списку
    1.1. если индекс нечетный тут нечего ловить
    1.2 если индекс четный
        1.2.1 проверить отриательный ли элемент под данным индексом и является ли он нечетны

'''

for i in range(len(number_list)):
    '''i = 0,1,2,3,....19'''
    if i % 2 == 0:
        if number_list[i] < 0 and number_list[i] % 2 != 0:
            print(number_list[i], end = " ")

            
