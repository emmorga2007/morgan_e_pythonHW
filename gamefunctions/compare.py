from gamefunctions import gamevars
	#we have a tie, no point in going further
		#we are comparing player to gamevars.computer
		#3 and 18 need to be manipulated


def compare(player):
	if player == gamevars.computer:
		print("Tie! try again")

	elif player =="quit":
		print("you choose to quit, Quitter!.")
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