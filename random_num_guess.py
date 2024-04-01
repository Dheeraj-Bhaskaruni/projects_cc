import random


def getRandomNumber():
    return random.randrange(1, 100)


# Update the code below to solve the problem
def giveHint(number, guess):
    if abs(guess - number) > 10:
        return "Cold"
    elif guess == number:
        return "Right"
    elif abs(guess - number) <= 10:
        return "Hot"


def runGuess():
    secretNumber = 50
    user_guess = int(input("Enter a number between 1 and 100: "))
    hint = giveHint(secretNumber, user_guess)
    if hint == "Right":
        print("You guessed it Right!")
    else:
        print(hint)


if __name__ == '__main__':
    runGuess()