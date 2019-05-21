def main():
    lst = input("Enter a list. ")
    lst = lst.replace("[", "")
    lst = lst.replace("]", "")
    lmnts = lst.split(",")
    lst = list(lmnts)

    x, y = fnl(lst)

    print(x, y)


def fnl(lst):
    return lst[0], lst[-1]



main()
