#import then random package so we can generate a random ai
from random import randint
from gamefunctions import winlose, gamevars, compare


while gamevars.player is False:
	print("=====================================\n")
	print("Computer Lives:",  gamevars.computer_lives,"/", gamevars.total_lives)
	print("Player Lives:", gamevars.player_lives,"/", gamevars.total_lives)
	print("=====================================\n")
	print("Choose your weapon!\n")
	player=input(" choose rock, paper, or scissors: \n")
	#start doing some logic and condition checking
	

	
	compare.compare(player)


	if gamevars.player_lives is 0:
		winlose.winorlose("lose")
		
	elif gamevars.computer_lives is 0:
		winlose.winorlose("won")
		

		
	else:
		player = False
		gamevars.computer = gamevars.choices[randint(0,2)]
	

