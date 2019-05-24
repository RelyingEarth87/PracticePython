def main():
    string  = input("Enter a string at least two words long. ")

    lst = string_to_list(string)

    final = list_to_string(lst)

    print(final)


def string_to_list(string):
    string = string.split()
    lst = list(string)

    return lst


def list_to_string(lst):
    lst.reverse()
    string = lst[0]

    for i in range(1, len(lst)):
        string = string + " " + lst[i]

    return string


main()
