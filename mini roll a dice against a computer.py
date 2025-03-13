import random
min_value =1
max_value =6
player_points=0
computer_points=0

while player_points <30 and computer_points<30:
    print("are u ready, player?")
    while True:
        specific_say="yes"
        player_input=input("enter here ur respond pls:").lower()
        if player_input == specific_say:
            break  # Exit the loop if the player says 'yes'
        else:
            print("Invalid input. Please type 'yes' to continue.")

    numbers=range(1,6)
    dice_choices=random.choice(numbers)
    compudice_choices=random.choice(numbers)
    print(f"the dice number for the player is:{dice_choices}")
    print(f"the dice number for the computer is:{compudice_choices}")
    if dice_choices >compudice_choices:
        print("what a good luck u have!! u actually won against the computer!")
    elif dice_choices ==compudice_choices:
        print("a lucky tie huh cool")
    else:    
        print("it look like u have a bad luck today")
    player_points+= dice_choices
    computer_points+=compudice_choices
    print(f"the player points is:{player_points}")
    print(f"the computer points is:{computer_points}")
    if player_points >=30:
        print("Congratulations, you've reached 60 points!")
        break
    elif computer_points >=30:
        print("u lost, good luck next time man")
        break
    elif computer_points ==30 and player_points==30:
        print("a tie huh, okay no one wins")