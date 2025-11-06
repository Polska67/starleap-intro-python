def play_rps():
    import getpass
    answer = input("rock paper scissors enter start to play")
    if answer == "start":
        play_rps
    elif answer == "quit":
        None
    else:
        print("please enter start or quit")
    print("Rock Paper Scissors")
    P1 = getpass.getpass('Player 1: ')
    P2 = getpass.getpass('Player 2: ')

    if P1 == "rock" and P2 == "rock":
        print("Invalid Argument: Both Players entered same input, please try again.")
    elif P1 == "rock" and P2 == "paper":
        print("Player 2 wins")
    elif P1 == "rock" and P2 == "scissors":
        print == ("Player 1 wins")
    elif P1 == "paper" and P2 == "rock":
        print == ("Player 1 wins")
    elif P1 == "paper" and P2 == "paper":
        print("Invalid Argument: Both Players entered same input, please try again.")
    elif P1 == "paper" and P2 == "scissors":
        print("Player 2 wins")
    elif P1 == "scissors" and P2 == "rock":
        print("Player 2 wins")
    elif P1 == "scissors" and P2 == "paper":
        print("Player 1 wins")
    elif P1 == "scissors" and P2 == "scissors":
        print("Invalid Argument: Both Players entered same input, please try again.")
    else: print("invalid argument: please enter rock, paper, or scissors.")



play_rps()
answer = input("would you like to play again")

if answer == "yes":
    play_rps
if answer == "no":
    None



