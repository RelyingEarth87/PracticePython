def main():
    print("Welcome to the Cows and Bulls Game!\n")
    print("You are trying to guess a four-digit number. For every digit you guess correctly in the correct place, you will get a cow, and for every digit guessed correctly in the wrong place, you will get a bull.\n")
    print("The first number cannot be 0 but the rest can, and there are no repeat digits in the number.\n")
    guess = int(input("Enter a  four-digit number: "))
    while guess < 1000 or guess > 9999:
        print("This is not a four-digit number.")
        guess = int(input("Enter a four-digit number: "))

    guess = str(guess)
    guesses = 1
    actual = str(game_start())  #generates number to start

    

    while guess != actual:
        if guess == "number":   #hidden give up option so people don't know unless they get super frustrated and look in code
            print("You have given up. ")
            break
        game = play(guess, actual)  #determines cows and bulls
            
        guess = int(input("Enter another four-digit number: "))
        while guess < 1000 or guess > 9999:
            print("This is not a four-digit number.")
            guess = int(input("Enter a four-digit number: "))

        guess = str(guess)
        guesses += 1

    print("It took you {0} guesses to guess the number {1}!".format(guesses, actual))


def game_start():   #Make starting number to guess
    from random import randrange
    lst = []

    num = randrange(1000, 10000)  #Generate 4-digit number
    x = str(num)  #number to string
    for i in x:  # identify and eliminate duplicates
        lst.append(i)
    for i in range(4):
        if lst[i] in lst[i+1:]:
            if i == 0:
                x = lst[i]
                while x in lst: 
                    x = str(randrange(1, 10))
                lst[i] = x
            else:
                x = lst[i]
                while x in lst:
                    x = str(randrange(0, 10))
                lst[i] = x

    actual = lst[0] + lst[1] + lst[2] + lst[3]
    

    return actual
        
def play(guess, actual):
    cows = 0
    bulls = 0
    
    for i in range(4):
        if guess[i] == actual[i]:   #checks if digit in right place
            cows += 1
        elif guess[i] in actual:    #checks if digit in wrong place but present in whole number
            bulls += 1

    print("{0} cows, {1} bulls".format(cows, bulls))


if __name__ == "__main__":
    main()
