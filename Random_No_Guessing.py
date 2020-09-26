import random
n = 20
chances = 10
guess = 0
to_be_guessed = int(n*random.random())+1
while (chances > 0):
    while guess != to_be_guessed:
        guess = int(input("Enter any number between 0 - 20 : "))

        if guess >= 21:
            print("Enter a valid number between 0-20\n")

        elif guess > 0 and guess < 21:
            if guess > to_be_guessed:
                print("Number is larger")
            elif guess < to_be_guessed:
                print("Number is lesser")
            chances = chances - 1
            if chances == 0:
                print("No more chances left")
                print("Game over")
                break

            print("Chances left : ", chances, "\n")

    else:
        print("Number is matched")
        print("Congrulation, You Won!!!")
        print("Chances left : ", chances, "\n")
        break




