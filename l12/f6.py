with open('input.txt', 'r+') as file:
    whole_line = file.readline()
    file.seek(2)
    line_from_2 = file.readline(15)
    whole_line = whole_line.replace(line_from_2, '*'*15)
    file.seek(2)
    file.write(whole_line)
    
    
    
