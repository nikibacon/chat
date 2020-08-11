
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


def split_file(lines):
    new = [[]]
    
    for line in lines:

        new.append(line.strip('\t\n\r').split())

         
    return new

def space_filter(lines):
    new = []
    Name = filter(None, lines)
    for line in Name:
        if len(line) >= 4: 
            new.append(line)
    
    
    print(new)
    return new



def convert2(lines):
    new = []
    person = None  #還不知道是什麼
    
    for line in lines:
        #print(line)
        if line[2] == '蓓萱ㄎㄎ':
            person = '蓓萱ㄎㄎ'
            new.append( line[0] + '---' + person + ':' + line[3])
            continue
        elif line[2] == '有容乃大':
            person = '有容乃大'
            new.append( line[0] + line[1] + '---' + person + ':' + line[3])
            continue    
        
    return new

def write_file(filename, lines):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt') 
    lines = convert(lines)
    write_file('output.txt', lines)



    lines = read_file('LINE_Chat.txt') 
    lines = split_file(lines)
    lines = space_filter(lines)
    lines = convert2(lines)
    #print(lines)
    write_file('Out_LINE_Chat.txt', lines)


main()