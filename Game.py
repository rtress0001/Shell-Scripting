import random
#Rock Paper Scissors
#Delare Variables for player 1 and computer
player = ''
computer = '' 
#make a while loop with a true flag
flag = True
while flag:
    #Ask for inputs from player and insure they are rock paper or scissors
    while True:
        player = input("Enter Rock, Paper or Scissors:")
        player = player.capitalize()
        if player == "Rock" or player == "Paper" or player == "Scissors":
            break
        print("Please try again to enter the correct input for the game")
    #Generate a random number to be converted into rock paper scissors
    random_number = random.randint(1, 3)
    #convert random int into Rock, Paper, Scissors
    if random_number == 1:
        computer = "Rock"
    elif random_number == 2:
        computer = "Paper"
    else:
        computer = "Scissors"
    print("computer picks", computer)
    #Check who wins rock paper scissors
    if player == computer:
        print("Its a Tie")
    if player == "Rock" and computer == "Scissors":
        print("Player Wins")
    if player == "Rock" and computer == "Paper":
        print("computer wins")
    if player == "Paper" and computer == "Rock":
        print("Player Wins")
    if player == "Paper" and computer == "Scissors":
        print("computer wins")
    if player == "Scissors" and computer == "Paper":
        print("Player Wins")
    if player == "Scissors" and computer == "Rock":
        print("computer wins")  
    #repeat the game unless break
    if input("Repeat the game Y/N:") == "N":
        break
