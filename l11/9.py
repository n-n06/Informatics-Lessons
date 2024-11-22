a = 1
count = 0

while a <= 1024:
    number = int(input("Введите число: "))
    a *= number
    count += 1
    print("Текущее произведение: ", a)

print(count)

