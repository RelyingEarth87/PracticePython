def main():
    num = int(input("Enter a number. "))

    x = isprime(num)

    if x == True:
        print("{0} is a prime number.".format(num))
    else:
        print("{0} is not a prime number.".format(num))

def isprime(num):
    i = 2
    while i <= num:
        if num == 2:
            return True
        elif i == num:
            return True
        elif num % i == 0:
            return False
        else:
            i += 1


main()
