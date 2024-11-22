

with open('text.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)
    all_lines = file.read()
    print(all_lines)

    file.seek(5)
    line3 = file.readline()
    print(line3)
