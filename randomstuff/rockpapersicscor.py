user_choice= input("Enter your choice, rock paper or scissors: ")

import random

options= ["rock","paper", "scissors"]
computer_choice = random.choice(options)
print("Computers choice: ", computer_choice)

if user_choice==computer_choice:
    print("its a tie!")
    
elif (user_choice=="rock" and computer_choice=="scissors") or\
    (user_choice=="scissors" and computer_choice=="paper") or\
    (user_choice=="paper" and computer_choice=="rock"):
    print("YOU WIN!")
else:
    print("COMPUTER WINS!")


