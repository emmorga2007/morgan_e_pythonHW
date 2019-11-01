#import then random package so we can generate a random ai
from random import randint

#"basket" of choices
choices=["rock", "paper", "scissors"]

#adding lives, when one or the ther gets to 0, win / lose
player_lives = 5
compter_lives = 5

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

	elif player =="rock":
		if computer == "paper":
			print("You Lose!", computer, "covers", player, "\n")
		else:
			print("You Won!", player, "smashes", computer, "\n")

	elif player =="paper":
		if computer == "scissors":
			print("You Lose!", computer, "cuts", player, "\n")
		else:
			print("You Won!", player, "covers", computer, "\n")

	elif player =="scissors":
		if computer == "rock":
			print("You Lose!", computer, "smashes", player, "\n")
		else:
			print("You Won!", player, "cuts", computer, "\n")


		

	player = False
	computer = choices[randint(0,2)]
	

