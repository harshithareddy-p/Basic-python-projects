import random

choices = ['r','p','s']
emojis = {'r':'🪨','p':'🧻','s':'✂️'}

print("---THE ROCK, PAPER, SCISSORS GAME---")

while True:
    user_choice = (input("Rock, paper, or scissors?(r/p/s): ")).lower()
    if(user_choice not in choices):
        print(" Invalid choice!")
        continue

    computer_choice= random.choice(choices)

    print(f'You choose {emojis[user_choice]}')
    print(f'Computer choose {emojis[computer_choice]}')
    
    if( user_choice == computer_choice):
        print("Its a tie")
    elif((computer_choice=='r' and user_choice=='p' or
        computer_choice=='s' and user_choice=='r' or
        computer_choice=='p' and user_choice=='s')):
        print("Woah, you won!✨")
    else :
        print("You lost 😒")
        
    continue_playing = input("wanna continue playing?(y/n): ").lower()
    if(continue_playing =='n'):
    break
