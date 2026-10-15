#import math library for random
import random

#defining function for get_choices
def get_choices():
    #keeping the loop running until a certain condition is met
    while True:
        options = ['rock', 'paper', 'scissors']

        player_response = input('Choose an option [Rock, Paper or Scissors]: ').strip().lower()

        if player_response not in [option.lower() for option in options]:
            print ("Invalid option, pick Rock, Paper or Scissors")
            continue
        else:
            computer_response = random.choice(options)
            return player_response, computer_response



def check_winner(player_response, computer_response):
    if player_response == computer_response:
        print ("There is a tie")
    elif player_response == 'rock' and computer_response == 'paper':
        print ('Computer Won')
    elif player_response == 'paper' and computer_response == 'scissors':
            print ('Computer Won')
    elif player_response == 'scissors' and computer_response == 'rock':
            print ('Computer Won')
    else:
         return 'You won'



def play_game():
    player_response, computer_response = get_choices()

    print(f"You chose: {player_response}")
    print(f"Computer chose: {computer_response}")

    result = check_winner(player_response, computer_response)
    print(result)


play_game()