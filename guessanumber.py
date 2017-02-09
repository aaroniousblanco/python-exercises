#creates a guess a number game. generates a random number, gives player five chances (counts down those chances), and tells player
#whether they're high or low. Asks player if they want to play again upon completion of each game. 
import random

play_again = "Y"

def game():
    guess_count = 5
    secret_number = random.randint(1, 10)
    while True:
        user_guess = int(raw_input("What's your number? "))
        if user_guess == secret_number:
            print "You win!"
            play_again = raw_input("Wanna play again? (y or n) ").upper()
            break
        elif user_guess < secret_number:
            print "%d is too low." % user_guess
            guess_count -= 1
            print "You have %d guesses left." % guess_count
        elif user_guess > secret_number:
            print "%d is too high." % user_guess
            guess_count -= 1
            print "You have %d guesses left." % guess_count
        if guess_count < 1:
            print "You ran out of guesses!"
            play_again = raw_input("Wanna play again? (y or n) ").upper()
            break

while True:
    if play_again == "Y":
        game()
    elif play_again == "N":
        print "Bye!"
        break
