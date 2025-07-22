user_guess=int(input("Guess the number from 1-10: "))


import random 
computer_choice = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

while user_guess != computer_choice:
    if user_guess>computer_choice:
            user_guess=int(input("Too high. Try again: "))
            
    elif user_guess<computer_choice:
            user_guess=int(input("Too low. Try again: "))
           
print("Congrats you got the right number!")
        