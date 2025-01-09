import random


options = ["rock", "paper", "scissor"]
computer_option = random.choice(options)
user_option = None

while True:
    computer_option = random.choice(options)
    user_option = None

    while user_option not in options:
        user_option = input("ENTER YOUR OPTIONS:").lower()
        if user_option not in options:
            print("option not available Choose Again")
    else:
        print(f"Computer Chose: {computer_option}")
        print(f"You Chose: {user_option}")
        
    if user_option == computer_option:
        print("Its a Tie")
    elif (user_option == "" and computer_option == "")or\
        (user_option == "" and computer_option == "")or\
        (user_option == "" and computer_option == ""):
        print("YOU WON !!!")
    else:
        print("COMPUTER WON !!!")

    another_round = input("you wanna play again : ").lower()
    if another_round != "yes":
        print("-----------CHEERS MATE !!!-------------")
        break
    

