num = int(input())

if num > 0 and num % 2 == 0:
    print("even positive")
elif num > 0 and num % 2 == 1:
    print("odd positive")
elif num == 0 or num < 0:
    print("useless")
