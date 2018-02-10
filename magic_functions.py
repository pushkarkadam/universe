import random


def get_menu():
	print("""
Please Enter the following:
To create: c
To destroy: d
To know thy creation: k
Quit program: q
		""")


def give_me_name():
	names = ["sum","dum","fri","kan","jar","far","sark","spo","ck","ls","kha","bitch","shee","koon"]
	first_syllable = random.choice(names)
	second_syllable = random.choice(names)
	return first_syllable+second_syllable


def give_me_race():
	races = ["humans","elves","orcs","dark elves","vulcans","romulans","klingons"]
	return random.choice(races)

def give_me_sex():
	sex = ["male","female"]
	return random.choice(sex)

def give_me_profession():
	professions = ["engineer","scientist","soldier","chef","wizard","captain","politician","Assassin","priest"]
	return random.choice(professions)

def give_me_powers():
	powers = ["nerve pinch","telepathy","potions","flight","time travel"]
	return random.choice(powers)
