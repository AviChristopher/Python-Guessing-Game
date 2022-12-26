import random
from statistics import mean
from statistics import mode
from statistics import multimode
from statistics import median


def start_game():
    print("Welcome to Guess the number game!!!") #Welcome message
    guess_number=0
    attempts=[]
    attempts.append(guess_number)
    random_number = random.randint(1, 100)

    while random_number != guess_number:
        try:
            guess_number = int(input("Guess a number between 1 and 100   "))
            if guess_number < 1 or guess_number >100:
                print("Please choose a number between 1 and 100")
        except ValueError:
            print("Oh no! You did not enter a number. Try again!! ")
        else:

            if guess_number > random_number:
                print("It's lower")
            elif guess_number < random_number:
                print("It's higher")
            else: # if user guessed right
                break
    attempts.append(guess_number)
    # using len(attempts) to get
    print("YOU WIN!You guessed {} times.".format(len(attempts)))
    print(f"The mean is {mean(attempts)}.\nThe median is {median(attempts)}.\nThe mode is {mode(attempts)}.")
    play_again = input("Do you want to play again. Yes/no  ")
    if play_again.lower()[0] == "y":
        start_game()
    else:
        print(u"\U0001F61E" "Sad to see you go. Come again !")

            # Kick off the program by calling the start_game function.

start_game()
