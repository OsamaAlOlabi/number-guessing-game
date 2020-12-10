import random


lives = 0

def user_start():
    global lives

    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 and 100. Can you guess it?")
    difficulty = input("Would you like to play on 'EASY' or 'HARD' mode?: ").lower()

    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5

    print(f"\nYou have this many tries {lives}")


def number_guessing_game():
    global lives

    while lives != 0:


        random_number = random.randint(1, 100)

        guess = int(input("Make a guess: "))

        if random_number == guess:
            print(f"YAY, you did it, You have {lives} tries left")
            play_again()
            break
        elif random_number > guess:
            if (random_number - guess) == 1:
                print("Are you serious? 1 NUMBER HIGHER")
                lives -= 1
            elif (random_number - guess) <= 5:
                print("Just a little higher")
                lives -= 1
            else:
                print("Go higher")
                lives -= 1
        elif random_number < guess:
            if (guess - random_number) == 1:
                print("Are you serious? 1 NUMBER LOWER")
                lives -= 1
            elif (guess - random_number) <= 5:
                print("Just a little lower")
                lives -= 1
            else:
                print("Go lower")
                lives -= 1

    if lives == 0:
        print(f"\nYou lost, the number was {random_number}")
        play_again()


def play_again():
    while True:
        user_input = input("Would you like to play again? 'Y' or 'N'?: ").lower()
        if user_input == "y":
            print('''
            
            
            
            
            
            
            
            
            
            
            
            
            
            ''')
            user_start()
            number_guessing_game()
            break
        elif user_input == "n":
            exit()
        else:
            print("Please type 'Y' or 'N'")

user_start()
number_guessing_game()