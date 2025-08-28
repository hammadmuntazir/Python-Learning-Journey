n=5
guess=0
while guess!=n:
    guess=int(input("Enter your guess:"))
    if guess==n:
        print("You won!")
    else:
        print("Guess again")

