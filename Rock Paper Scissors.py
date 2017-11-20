print ("Welcome to the Rock, Paper, Scisors Simulator. Pick 1 for rock, 2 for paper and 3 for scissors.")

print ("This game is best of five so good luck")

import sys

import random

plr_score = 0

comp_score = 0

winner = "meme"

while plr_score < 5 and comp_score < 5:

    player = input("Your Choice, one, two or three?")

    player = int(player)

    computer = random.uniform(1,3)

    computer = int(computer)

    print ("The computer got %s." % computer)

    if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:

        winner = "The Player Wins!"

        print (winner)

    else:

        if player == 3 and computer == 1 or player == 1 and computer == 2 or player == 2 and computer == 3:

            winner = "The Computer Wins!"

            print (winner)
            
        else:

            if player == 1 and computer == 1 or player == 2 and computer == 2 or player == 3 and computer == 3:

                winner = "Nobody Wins!"

                print (winner)


    if winner == "The Player Wins!":

        plr_score = plr_score + 1

    if winner == "The Computer Wins!":

        comp_score = comp_score + 1

    print ("You currently have %s points" % plr_score)

    print ("The computer has %s points." % comp_score)

    if plr_score == 5 or comp_score == 5:

        print ("The game's over, check and see who won. See ya later.")

        sys.exit()
