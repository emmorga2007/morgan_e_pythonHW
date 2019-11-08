from random import randint

#"basket" of choices
choices=["rock", "paper", "scissors"]

#adding lives, when one or the ther gets to 0, win / lose
player_lives = 1
computer_lives = 1
total_lives = 1 

#let the AI make choices
computer=choices[randint(0,2)]

#set up a game loop here so we don't have to keep restarting
player= False