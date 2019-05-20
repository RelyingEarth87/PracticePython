def main():
    print("Rock, Paper, or Scissors. Best 2 out of 3. GO!")
    start = 0

    while start == 0:
        score_a = 0
        score_b = 0
        while score_a <2 and score_b < 2:
            p1 = input("Player 1, what will you throw? ")
            p2 = input("Player 2, what will you throw? ")

            print("\nRock, Paper, Scissors, SHOOT!\n")

            p1 = p1.lower()
            p2 = p2.lower()

            if p1 == "rock":
                p1 = 1
            elif p1 == "scissors":
                p1 = 2
            elif p1 == "paper":
                p1 = 3

            if p2 == "rock":
                p2 = 1
            elif p2 == "scissors":
                p2 = 2
            elif p2 == "paper":
                p2 = 3

            if p1 == p2:
                print("It's a tie!\n")
            elif p1 == 1:
                if p2 == 2:
                    score_a += 1
                    print("Player 1 wins with Rock over Scissors")
                elif p2 == 3:
                    score_b += 1
                    print("Player 2 wins with Paper over Rock")
            elif p1 == 2:
                if p2 == 1:
                    score_b += 1
                    print("Player 2 wins with Rock over Scissors")
                elif p2 == 3:
                    score_a += 1
                    print("Player 1 wins with Scissors over Paper")
            elif p1 == 3:
                if p2 == 1:
                    score_a += 1
                    print("Player 1 wins with Paper over Rock")
                elif p2 == 2:
                    score_b += 1
                    print("Player 2 wins with Scissors over Paper")
        
        if score_a == 2:
            print("\nPlayer 1 wins!")
        elif score_b == 2:
            print("\nPlayer 2 wins!")
        start = int(input("\nWould you like to play again? (0 = Yes, 1 = No) "))

    else:
        print("Game over! Play Again Soon!")


main()
