#import then random package so we can generate a random ai
from random import randint

#"basket" of choices
choices=["rock", "paper", "scissors"]

#adding lives, when one or the ther gets to 0, win / lose
player_lives = 1
computer_lives = 1

#let the AI make choices
computer=choices[randint(0,2)]

#set up a game loop here so we don't have to keep restarting
player= False

def winorlose(status):
	print("called win or lose", status)
	print("You", status, "! Would you like to play again?")
	choice = input("Y / N")

	if choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global player
		global computer
		
		player_lives = 1
		computer_lives = 1
		player = False
		computer = choices[randint(0,2)]
		
	elif choice == "N" or choice == "n":
		print("You choose to quit.")
		exit()
	else:
		print("make valid choice, yes or no?")


while player is False:
	print("=====================================\n")
	print("Computer Lives:", computer_lives, "/1\n")
	print("Player Lives:", player_lives, "/1\n")
	print("=====================================\n")
	print("Choose your weapon!\n")
	player=input(" choose rock, paper, or scissors: \n")
	#start doing some logic and condition checking
	

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
			player_lives = player_lives -1
		else:
			print("You Won!", player, "smashes", computer, "\n")
			computer_lives = computer_lives -1

	elif player =="paper":
		if computer == "scissors":
			print("You Lose!", computer, "cuts", player, "\n")
			player_lives = player_lives -1
		else:
			print("You Won!", player, "covers", computer, "\n")
			computer_lives = computer_lives -1

	elif player =="scissors":
		if computer == "rock":
			print("You Lose!", computer, "smashes", player, "\n")
			player_lives = player_lives -1
		else:
			print("You Won!", player, "cuts", computer, "\n")
			computer_lives = computer_lives -1

	if player_lives is 0:
		winorlose("lost")
		#print("you lost! Loserrr. Would you like to play again?")
		#choice = input("Y / N")

		#if choice == "Y" or choice == "y":
		#reset game to start again
		# 	player_lives = 1
		# 	computer_lives = 1
		# 	player = False
		# 	computer = choices[randint(0,2)]
		
		# elif choice == "N" or choice == "n":
		# 	print("You choose to quit.")
		# 	exit()
		# else:
		# 	print("make valid choice, yes or no?")


	elif computer_lives is 0:
		winorlose("win")
		# print("You won! Would you like to play again?")	
		# choice = input("Y / N")

		# if choice == "Y" or choice == "y":
		# #reset game to start again
		# 	player_lives = 1
		# 	computer_lives = 1
		# 	player = False
		# 	computer = choices[randint(0,2)]
		
		# elif choice == "N" or choice == "n":
		# 	print("You choose to quit.")
		# 	exit()
		# else:
		# 	print("make valid choice, yes or no?")


		
	else:
	player = False
	computer = choices[randint(0,2)]
	

