import random

def main():
	global cred
	cred = 50000
	mainscreen()

def mainscreen():
	print("""    	   ________            
	  /\       \           
	 /o \   o   \          
	/    \_______\         
	\    /o      /         
	 \o /   o   /          
	  \/_____o /
	""")
	print("Welcome to World Series of Dice!")
	print("Try and guess the outcome of 2 dices!")
	print("In order to quit, press ctrl + c\n")
	print("You currently have",cred,"$"'\n')
	print("What would you like to do?\n\nType 1 if you would like to start the game\nType 2 if you need more credits\nType 3 if you want to see the rules\n")
	try:
		choice = int(input("Please type your selection: "))
	except ValueError:
		print("\nOnly numbers are allowed\n")
		mainscreen()

	if choice == 1:
		gamestart()

	if choice == 2:
		addcred()
		gamestart()

	if choice == 3:
		rules()
		mainscreen()

	if choice != 1 and choice != 2 and choice != 3:
		print("Wrong choice\n")

def rules():
	print("----------------------------")
	print("Here is your ruleset:\n")
	print("Your regular payoff is 5 to 1\nIf you roll 7 and guess it correctly, then your payoff is 10 to 1\nIf you roll 7 and do not guess it, you do not lose your bet\nIf you roll 2 without betting on it, you lose\n")
	print("----------------------------")
	mainscreen()

def gamestart():
	global cred
	print("\nType main in roll selection if you would like to go back to main screen")
	while True:

		print("You currently have",cred,"$"'\n')

		x = random.randrange(2, 12)

		try:
			bet = int(input("Enter amount of $ you would like to bet: "))
		except ValueError:
			print("Only numbers are allowed\n")
			gamestart()

		guess = input("Enter number between 2 and 12: ")

		if guess == "main":
			mainscreen()

		if int(bet) > cred:
			print("You do not have enough credits")
			gamestart()

		if bet == "back" or guess == "back":
			mainscreen()

		if guess == '2' or guess == '3' or guess == '4' or guess == '5' or guess == '6' or guess == '7' or guess == '8' or guess == '9' or guess == '10' or guess == '11' or guess == '12':
			print("The number was: ",x)

			if guess == str(x) and x == 2:
				cred = cred
				print("Snake eyes..!")
				print("Lucky, you do not lose anything\n")
				

			if guess != str(x) and x == 2:
				cred = cred - int(bet)
				print("Snake eyes..!")
				print("Unlucky... Better roll next time!\n")

			if guess == str(x) and x != 7 and x != 2:
				cred = cred + (int(bet) * 5)
				print("You win!\n")
				print("You currently have",cred,"$"'\n')

			if guess == str(x) and (x == 7):
				cred = cred + (int(bet) * 10)
				print("You win big time!\n")

			if guess != str(x) and x == 7:
				cred = cred
				print("Lucky 7!")
				print("You do not lose anything!\n")

			if guess != str(x) and x != 7 and x != 2:
				cred = cred - int(bet)
				print("You lose...\n")

		else:
			print("Wrong input")

		if cred <= 0:
			print("Better luck next time!")
			mainscreen()

def addcred():
	global cred
	cred = cred + 50000
	print("Bank is generous today, your account was granted 50000$!")
	mainscreen()

main()