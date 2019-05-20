def main():
    from random import randrange
    ext = 0
    tries = 0

    while ext != 1:
        num = int(input("What number am I thinking of from 1-9? "))
        if num > 9:
            raise ValueError("Invalid input.")

        comp = randrange(1, 10)
        
        if num > comp:
            print("You guessed too high.")
        elif num == comp:
            print("You guessed exactly right!")
        elif num < comp:
            print("You guessed too low.")

        tries += 1
        ext = int(input("\nWould you like to try again? (1 = No, 0 = Yes) "))

    print("You played {0} times.".format(tries))


main()
