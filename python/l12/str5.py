
number = input()
if number.isdigit():
    number = int(number)

    number *= number
    print(number)
else:
    print("Please, input a number")
