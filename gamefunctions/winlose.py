from random import randint
from gamefunctions import gamevars


def winorlose(status):
	print("called win or lose", status)
	print("You", status, "! Would you like to play again?")
	choice = input("Y / N")

	if choice == "Y" or choice == "y":
		
		gamevars.player_lives = 1
		gamevars.computer_lives = 1
		gamevars.player = False
		gamevars.computer = gamevars.choices[randint(0,2)]
		
	elif choice == "N" or choice == "n":
		print("You choose to quit.")
		exit()
	else:
		print("make valid choice, yes or no?")
			#recursion function= calling a function from inside itself 
		winorlose(status)