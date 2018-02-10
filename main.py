import random
from populate import Humanoids
from magic_functions import *
from got_power import *

print("""\n\n\n
	*******************************************************************************
	You are the creator of this Universe.\n
	Right now you have the ability to create humanoids in this universe.\n
	Just to make things easier for you, just input the population of your universe.\n

	                       ********  REMEMBER  *********
	The creation of your universe will be dependent upon your computing power
	So, harness the energy of the ether, and let the computations begin
	*******************************************************************************""")
balance = 1
while (balance):
	get_menu()
	user_value = input(">> ")

	if user_value == 'c' or user_value =='C':			#Creation
		creation_list = creation()
	elif user_value == 'd' or user_value == 'D':		#destruction
		try:
			destroy(creation_list)
			break
		except NameError:
			print("You have not created anything!")
			continue
	elif user_value == 'k' or user_value == 'K':		#Introduction
		try:
			know_thy_creation(creation_list)
		except NameError:
			print("You have not created anything!")
			continue
	elif user_value == 'q' or user_value == 'Q':		#Exit
		balance = 0
	else:
		print("Incorrect input! Try again!")
		continue
	