from random import randint
player_wins = 0
computer_wins = 0
default_winning_score = 3
print("***ROCK***")
print("***PAPER***")
print("***SCISSORS***")
print("Win Points --> 1")
print("Lose Points --> 0")
plays =  ["rock", "paper", "scissors", "q", "quit"]
try:
    winning_score = int(input("Enter a Winning Score : "))
except:
    winning_score = default_winning_score
    print("Invalid Input")
    print("Winning score has set to 3 by default")
while player_wins < winning_score and computer_wins < winning_score:
    print(f"player score:{player_wins} computer score:{computer_wins} ")
    print("Type q (or) quit to exit :( DON'T CHOOSE ME PLEASE")

    player = input("player make your move! ------> rock || paper || scissors :").lower()
    if player not in plays:
    	print("Please enter a valid input")
    	continue

    if player == "quit" or player == "q":
        break
    rand_num = randint(0,2)
    if rand_num == 0:
        computer ="rock"
    elif rand_num == 1:
        computer ="paper"
    else:
        computer ="scissors"
    print(f"computer plays {computer}")
    if player == computer:
        print( "It's a tie!")
    elif player == "rock":
        if computer =="paper":
            print("oops computer wins! keep playing")
            computer_wins += 1
        else:
            print("WINNER WINNER CHICKEN DINNER!!!")
            player_wins += 1
    elif player == "paper":
        if computer =="rock":
            print("WINNER WINNER CHICKEN DINNER!!!")
            player_wins += 1
        else:
            print("oops computer wins! keep playing")
            computer_wins += 1
    elif player == "scissors":
        if computer =="paper":
            print("WINNER WINNER CHICKEN DINNER!!!")
            player_wins += 1
        else:
            print("oops computer wins! keep playing")
            computer_wins += 1
    else:
        print("something went wrong")
    print("---------------------------------------------------------------------------")
if player_wins<computer_wins:
    print("OOPS! BETTER LUCK NEXT TIME  COMPUTER WON!!!!!")
elif player_wins==computer_wins:
    print("it's a tie")
else:
    print("THE GODS OF THIS GAME ARE IN AWE!!!! AND SHOCK!!!!!! \n YOU WON :)")
              
print(f"FINAL SCORES : player score : {player_wins} computer score : {computer_wins}")
