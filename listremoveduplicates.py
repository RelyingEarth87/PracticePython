def main():
    from random import randrange
    x = randrange(6, 25)

    lst = generate(x)
    print(lst)

    new = remove_dupes(lst)

    print(new)


def generate(num):
    from random import randrange
    lst = []
    
    for i in range(0, num):
        x = randrange(0, 100)
        lst.append(x)

    return lst


def remove_dupes(lst):
    lst.sort()
    i = 0

    while i < len(lst) - 1:
        if lst[i] == lst[i + 1]:
            lst.pop(i)
        i += 1

    return lst


main()
