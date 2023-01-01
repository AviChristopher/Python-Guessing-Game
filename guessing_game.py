import random
from statistics import mean
from statistics import mode
from statistics import multimode
from statistics import median

att_list=[]

def start_game():
    print("Welcome to Guess the number game!!!") #Welcome message
    guess_number=0 
    li=[]
    attempts=[]
    random_number = random.randint(1, 100) 
    
    while True:
        try:
            guess_number = int(input("Guess a number between 1 and 100   "))
            li.append(guess_number)
            if guess_number < 1 or guess_number >100:
                print("Please choose a number between 1 and 100")
        except ValueError:
            print("Oh no! You did not enter a number. Try again!! ")
        else:
            
            if guess_number > random_number:
                print("It's lower")
                continue
            elif guess_number < random_number:
                print("It's higher")
                continue
            elif guess_number ==  random_number:
                
                               
                print(f"YOU WIN!You guessed {len(li)} time(s)")
                print(f" Here are your guesses:{li}")
                leng= len(li)
                attempts.append(leng)
                att_list.append(attempts[0])
                median_score=median(att_list)
                mode_score=multimode(att_list)
                average_score=mean(att_list)                             
                                
                print(f"The mode of your score is:{mode_score}")
                print(f"The mean of your score is:{average_score}")
                print(f"The median of your score is:{median_score}")
                print(">>>>>Attempt Score<<<<<")
                print(att_list)
                print("Do you think you can beat this score?")           
            play_again = input("Play again. Y/N  ").lower() 
            if play_again   == 'Y' or play_again == 'y':
                print(">>>>>HIGHSCORE<<<<<")
                print(f">>>The least number of guesses: {min(att_list)} ")
                start_game()  
            else:
                print(u"\U0001F61E" "Sad to see you go. Come again !")
            break
                
            # Kick off the program by calling the start_game function.

start_game()
