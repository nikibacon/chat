
def read_file(filename):
    lines = []
    with open (filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None  #還不知道是什麼
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue    
        if person:  #如果有值才會進入
            new.append(person + ':' + line)
    return new


def print_file(lines):
    for line in lines:
        print(line)


def write_file(filename, lines):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt') 
    lines = convert(lines)
    write_file('output.txt', lines)



    #lines = read_file('LINE_Chat.txt') 
    #print_file(lines)
    #write_file('Out_LINE_Chat.txt', lines)


main()