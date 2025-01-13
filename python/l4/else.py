
a = int(input())
b = int(input())

# a = 2, b = 13
for i in range(a, b + 1):
    #i = 2,3,4,5,....,13
    if i % 5 == 0:
        continue
    elif i == 14:
        break
    else:
        print(i)


    #some code#
    #....
    #...
    #...
else:
    print("The cycle is finished without problems! ;)")
#...other code
