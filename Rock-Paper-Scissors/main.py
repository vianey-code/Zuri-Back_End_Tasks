import random

print('Welcome to the Rock Paper Scissors Game!')
print('The rules of the game are :')
print('Rock smashes scissors')
print('Paper covers rock')
print('Scissors cut paper')
print("Let's get started!")
possible_choices =['R' , 'P' ,'S']
while True:

    user_choice = input('Enter a choice (R for Rock , P for Paper, S for Scissors) : ')
    if user_choice not in possible_choices:
        print("invalid choice")
    else:
        pass

        name_choices = ''
        
        if user_choice =="R":
            name_choices ='Rock'
        elif user_choice == "S":
            name_choices ='Scissors'
        elif user_choice == "P":
            name_choices ='Paper'
            
        
        computer_choice = random.choice(possible_choices)
        computer_choices = ""

        if computer_choice == "R":
            computer_choices="Rock"
        elif computer_choice == "S":
            computer_choices="Scissors"
        elif computer_choice == "P":
            computer_choices="Paper"
        
        
        print(f"player ({name_choices}) : CPU ({computer_choices})")

        if user_choice == "R":
            if computer_choice =='S':
                print('Rock smashes scissors , you win!')
            elif computer_choice == "P":
                print('Paper cover rock, computer wins!')
        elif user_choice == 'S':
            if computer_choice == 'P':
                print('Scissors cuts paper , you win!')
            elif computer_choice == "R":
                print('Rock smashes scissors, computer wins!')
        elif user_choice == 'P':
            if computer_choice == 'R':
                print('Paper covers rock, you win!')
            elif computer_choice == "S":
                print('Scissors cuts paper, computer wins!')
        if user_choice == computer_choice:
            print('This is a tie,play again!')
        else:
            print('Thanks for playing!')
            break
