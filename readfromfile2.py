def main():
    file_names = []
    
    filename = "Training_01.txt"

    file = open(filename, 'r')

    line = file.readline()
    line = line.strip()
    line = line.split("/")
    type_ = line[2]
    file_names.append(type_)

    while line != '':
        line = file.readline()
        line = line.strip()
        line = line.split("/")
        try:
            type_ = line[2]
            file_names.append(type_)
        except:
            break
        

    number = count(file_names)

    print(number)

def count(names):
    counter = {}

    for i in names:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    return counter


main()
