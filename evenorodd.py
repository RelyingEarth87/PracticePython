def main():
    num = int(input("Enter a number: "))
    check = int(input("Input another number to divide the first number by: "))


    if num % 4 == 0:
        print("{0} is divisible by four.".format(num))
    elif num % 2 == 0:
        print("{0} is an even number.".format(num))
    else:
        print("{0} is an odd number.".format(num))


    if num % check == 0:
        print("{0} divides evenly into {1}.".format(check, num))
    else:
        print("{0} does not divide evenly into {1}.".format(check, num))


main()
