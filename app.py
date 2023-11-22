# create a variable called computer that is assigned a random option between 'rock', 'paper', or 'scissors'
import random
# HINT: use random.choice()
computer = random.choice(['rock', 'paper', 'scissors'])
# create a variable called winner and assign it a value of None
winner = None
# create a variable called valid that accepts a boolean value
valid = True;
# create a playercount variable and assign it a value of 0
playercount = 0
#create a computercount variable and assign it a value of 0
computercount = 0
# create a while loop that will run until the user enters a stop 
# value of 'q' or 'Q'
while valid == True:
    # create a variable called user_input that prompts the user to
    # enter a string or 'q' to quit
    user_input = input("Enter a rock, paper, scissors or 'q' to quit: ")
    user_input = user_input.lower()
    # create a try/except block that will check if the user entered 'rock','paper', 'scissors' or 'q'
    # if the user entered 'rock','paper', 'scissors' or 'q' set valid to True
    # else print "Invalid input"
    try:
        if user_input == 'rock' or user_input == 'paper' or user_input == 'scissors' or user_input == 'q':
            valid = True
        else:
            print("Invalid input")
    except:
        print("Invalid input")
    # create an if/elif/else block that will check if the user entered 'q'
    if user_input == 'q':
    #set valid to False
        valid = False
        # if the user entered 'q' print who won the game and the score
        print("User score: " + str(playercount))
        print("Computer score: " + str(computercount))
        if playercount > computercount:
            print("User wins the game")
        elif playercount < computercount:
            print("Computer wins the game")
        else:
            print("It's a tie")
    # elif the user entered 'rock' check if the computer is 'paper' or 'scissors'
    elif user_input == 'rock':
        if computer == 'paper':
            # increment the computercount variable by 1
            computercount += 1
            print("Computer wins with paper")
        elif computer == 'scissors':
            # increment the playercount variable by 1
            playercount += 1
            print("User wins with rock")
        else:
            print("It's a tie")
    # elif the user entered 'paper' check if the computer is 'rock' or 'scissors'
    elif user_input == 'paper':
        if computer == 'rock':
            # increment the playercount variable by 1
            playercount += 1
            print("User wins wit rock")
        elif computer == 'scissors':
            # increment the computercount variable by 1
            computercount += 1
            print("Computer wins with scissors")
        else:
            print("It's a tie")
    # elif the user entered 'scissors' check if the computer is 'rock' or 'paper'
    elif user_input == 'scissors':
        if computer == 'rock':
            # increment the computercount variable by 1
            computercount += 1
            print("Computer wins with rock")
        elif computer == 'paper':
            # increment the playercount variable by 1
            playercount += 1
            print("User wins with scissors")
        else:
            print("It's a tie")



