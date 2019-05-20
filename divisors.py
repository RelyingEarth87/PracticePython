def main():
    a = int(input("Enter a number: "))
    b = []

    for i in range(1, a + 1):
        if a % i == 0:
            b.append(i)
        else:
            pass

    print("The possible divisors of {0} are {1}.".format(a, b))


main()
