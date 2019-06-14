def main():
    names = []
    
    filename = "nameslist.txt"

    file = open(filename, 'r')

    line = file.readline()
    line = line.strip()
    names.append(line)

    while line != '':
        line = file.readline()
        line = line.strip()
        names.append(line)

    number = count(names)

    print(number)


def count(names):
    counter = {}

    for i in names:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    return counter

    
    
