def main():
    lst = input("Enter an ordered list of numbers. If you would like a premade list, type 0000 ")
    num = int(input("What number would you like to compare? "))

    if lst == "0000":
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    else:
        numbers = manipulate(lst)
    result = search(numbers, num)

    print(result)

    


def manipulate(lst):
    numbers = []

    lst = lst.split(", ")

    
    a = lst[0].split("[")
    lst[0] = a[1]
    
    b = lst[-1].split("]")
    lst[-1] = b[0]

    for i in lst:
         numbers.append(int(i))
    

    return numbers


def search(lst, num):
    if num in lst:
        return True
    else:
        return False


main()
