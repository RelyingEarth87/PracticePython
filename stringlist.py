def main():
    x = input("Please enter a word: ")

    z = x.lower()
    
    for i in range(len(z)):
        if z[i] == z[-(i + 1)]:
            f = True
        else:
            f = False
            break


    if f == True:
        print("{0} is a palindrome.".format(x))
    else:
        print("{0} is not a palindrome.".format(x))


main()
