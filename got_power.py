from populate import Humanoids
from magic_functions import *

def creation():
		populus = int(input("Enter the number of Humanoids you wish to create: "))

		limit = list(range(0,populus))
		creations = []

		for x in limit:
			name = give_me_name()
			race = give_me_race()
			sex = give_me_sex()
			profession = give_me_profession()
			powers = give_me_powers()
			x = Humanoids(name,race,sex,profession,powers)
			creations.append(x)
		return creations

def know_thy_creation(creation_list):
	index = list(range(0,len(creation_list)))
	for x in index:
		creation_list[x].introduction()


def destroy(creation_list):
	index = list(range(0,len(creation_list)))
	for x in index:
		creation_list[x].die()
	print("No one left in this universe!")