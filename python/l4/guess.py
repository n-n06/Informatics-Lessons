print("Загадайте число")

# 1 - 100
# > 50
# 50 - 100
# > 75
# 75 - 100
# < 87
# 76 - 86
# < 81
# 76 - 80
# < 78
# 77

left = 0
right = 100

while True:
    print("Ваше число равно ", (left + right) // 2)
    answer = input()
    if answer == "yes":
        print("Nah I'd win")
        break

    print("Ваше число больше чем ", (left + right) // 2)
    answer = input()
    if answer == "yes":
        left = (left + right) // 2
        continue
    
    right = (left + right) // 2



