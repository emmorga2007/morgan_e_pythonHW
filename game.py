#import then random package so we can generate a random ai
from random import randint
from gamefunctions import winlose, gamevars


while gamevars.player is False:
	print("=====================================\n")
	print("Computer Lives:",  gamevars.computer_lives,"/", gamevars.total_lives)
	print("Player Lives:", gamevars.player_lives,"/", gamevars.total_lives)
	print("=====================================\n")
	print("Choose your weapon!\n")
	player=input(" choose rock, paper, or scissors: \n")
	#start doing some logic and condition checking
	

	#always check a breaking condition first
	if player == gamevars.computer:
		#wehave a tie, no point in going further
		print("tie, no one wins! try again")

	elif player == "quit":
		print("you choose to quit, quitter.")
		exit()

	elif player =="rock":
		if gamevars.computer == "paper":
			print("You Lose!", gamevars.computer, "covers", gamevars.player, "\n")
			gamevars.player_lives = gamevars.player_lives -1
		else:
			print("You Won!", player, "smashes", gamevars.computer, "\n")
			gamevars.computer_lives = gamevars.computer_lives -1

	elif player =="paper":
		if gamevars.computer == "scissors":
			print("You Lose!", gamevars.computer, "cuts", player, "\n")
			gamevars.player_lives = gamevars.player_lives -1
		else:
			print("You Won!", player, "covers", gamevars.computer, "\n")
			gamevars.computer_lives = gamevars.computer_lives -1

	elif player =="scissors":
		if gamevars.computer == "rock":
			print("You Lose!", gamevars.computer, "smashes", player, "\n")
			gamevars.player_lives = gamevars.player_lives -1
		else:
			print("You Won!", player, "cuts", gamevars.computer, "\n")
			gamevars.computer_lives = gamevars.computer_lives -1

	if gamevars.player_lives is 0:
		winlose.winorlose("lose")
		


	elif gamevars.computer_lives is 0:
		winlose.winorlose("won")
		

		
	else:
		player = False
		gamevars.computer = gamevars.choices[randint(0,2)]
	

