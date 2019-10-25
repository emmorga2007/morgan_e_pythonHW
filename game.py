#import then random package so we can generate a random ai
from random import randint

#"basket" of choices
choices=["rock", "paper", "scissors"]

#let the AI make choices
computer=choices[randint(0,2)]

#set up a game loop here so we don't have to keep restarting
player= False

while player is False:
	player=input(" choose rock, paper, or scissors: \n")
	#start doing some logic and condition checking
	print("computer: ", computer, "player: ", player)

	#always check a breaking condition first
	if player == computer:
		#wehave a tie, no point in going further
		print("tie, no one wins! try again")

	elif player == "quit":
		print("you choose to quit, quitter.")
		exit()

	else:
		print("NOT a tie. Now we can check other conditions")
		if player =="rock":
			print("check and see what the computer is, and win or lose")

	player = False
	computer = choices[randint(0,2)]
	

