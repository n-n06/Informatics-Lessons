file_input = open('input.txt', 'r')
file_output = open('output.txt', 'w')

a = int(input("Number of letters: ")) #4
n = int(input("Number of digits: ")) #4

first_line = file_input.readline(a)
file_input.readline()
second_line = file_input.readline(n)

file_output.write(first_line + '\n')
file_output.write(second_line)

file_input.close()
file_output.close()

