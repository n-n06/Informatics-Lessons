x = 2
z = 1

# x = 2, z = 1
# 1 iter 2 < 100 
    # x = 2 * 4 + 1 = 9
    # z = 1 + 9 = 10
    # print(x) -> 9
# 2 iter 9 < 100
    # x = 36 + 10 = 46
    # z = 46 + 10 = 56
    # print(x) -> 46
# 3 iter 46 < 100
    # x = 184 + 56 = 240
    # z = 240 + 56 = 296
    # print(x) -> 240
# 4 iter 240 < 100
    # end of the cycle
    # exit


while x < 100:
    x = x * 4 + z
    z += x

    if x == 46:
        continue

    print(x)
