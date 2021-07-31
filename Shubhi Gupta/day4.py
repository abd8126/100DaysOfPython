import random
print("Winning Rules of the Rock paper scissor game as follows: \n"+"Rock vs paper->paper wins \n"+ "Rock vs scissor->Rock wins \n"
								+"paper vs scissor->scissor wins \n")        #instruction of game

while True:
	print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")            #choice plate
	choice = int(input("Your turn: "))                                       #input from user
	while choice > 3 or choice < 1:                                          #loop for checking the valid in put from user
		choice = int(input("enter valid input: "))
	if choice == 1:                                                          # choice output
		choice_name = 'Rock'
	elif choice == 2:
		choice_name = 'paper'
	else:
		choice_name = 'scissor'
		
	print("your choice is: " + choice_name)                                  #user choice
	print("\nNow coputer will choose..")
	com_choice = random.randint(1, 3)
	while com_choice == choice:                                             # looping for computer input other then user's
		com_choice = random.randint(1, 3)
	if com_choice == 1:
		com_choice_name = 'Rock'
	elif com_choice == 2:
		com_choice_name = 'paper'
	else:
		com_choice_name = 'scissor'
		
	print("Computer choice is: " + com_choice_name)                          #computer choice output

	print(choice_name + " V/s " + com_choice_name)

	                                                                        # condition for winning
	if((choice == 1 and com_choice == 2) or
	(choice == 2 and com_choice ==1 )):
		print("paper wins = ", end = "")
		result = "paper"
		
	elif((choice == 1 and com_choice == 3) or
		(choice == 3 and com_choice == 1)):
		print("Rock wins =", end = "")
		result = "Rock"
	else:
		print("scissor wins =", end = "")
		result = "scissor"

	                                                                        # result declaration
	if result == choice_name:
		print(" You wins!!! ")
	else:
		print(" Computer wins !!!")
		
	print("Do you want to play again? (Y/N)")
	ans = input()
	if ans == 'n' or ans == 'N':                                              #condition for playing again
		break
print("\nThanks for playing")
