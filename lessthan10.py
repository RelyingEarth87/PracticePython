def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    d = []
    

    for i in a:
        if i < 5:
            b.append(i)
        else:
            pass

    print("The numbers in this list less than 5 are:", b)

    c = int(input("Enter a number to find elements in the list up to. "))

    for i in a:
        if i < c:
            d.append(i)
        else:
            pass

    print("The numbers in this list less than {0} are:".format(c), d)


main()
