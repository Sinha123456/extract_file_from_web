import random
def guessGame(a,b, actual):
    guess = int(input(f"Guess a number between {a} and {b}\n"))
    nguess = 1
    while nguess!= actual:
        if guess<actual:
            guess = int(input("Enter a bigger number\n"))
            nguess += 1
        else:
            guess = int(input("Enter a smaller number"))
            nguess += 1
    print(f"you guessed  number in "
          f"{nguess} guesses\n")
    return nguess

if __name__ == "__main__":
    a = int(input("Enter the value of a\n"))
    b = int(input("Enter the value of b\n"))
    actual1 = random.randint(a,b)
    print("Players 1's turn\n")
    g1 = guessGame(a, b, actual1)
    print("Player 2's turn\n")
    actual2 = random.randint(a,b)
    g2 = guessGame(a,b, actual2)
    if g1<g2:
        print("Player 1 won the match")
    if g1>g2:
        print("Player 2 won the match")
    else:
        print("Match is tie!")
    print(f"number for Player 1 is {actual1}  number for Player 2 is {actual2}")