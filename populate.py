import random
class Humanoids:
    
    population = 0
    
    def __init__(self, name, race, sex, profession, powers):
        self.name = name
        self.race = race
        self.sex = sex
        self.profession = profession
        self.powers = powers
        
        Humanoids.population += 1
        
        
    def die(self):
        print("{} is off the grid!".format(self.name))
        Humanoids.population -= 1
        
        if Humanoids.population == 0:
            print("{} was the last humanoid on the grid".format(self.name))
        elif Humanoids.population == 1:
            print("{} is the only humanoid on the grid.".format(Humanoids.population))
        else:
            print("There are still {} humanoids on the grid.".format(Humanoids.population))
            
    
    def introduction(self):
        print("\n\n******************************")
        print("Hello, My name is {}".format(self.name))
        print("I am categorised as {}".format(self.sex))
        
        dice_roll = random.random()*100
        if dice_roll <= 50:
            print("I do not wish to talk about my race. I believe in equality.")
        else:
            print("My people are called {}".format(self.race))
        print("I am {} by profession.".format(self.profession))
        print("My super power is {}".format(self.powers))
        print("******************************")
        
    @classmethod
    def how_many(cls):
        if cls.population > 1:
            print("There are {:d} humanoids on the grid.".format(cls.population))
        else:
            print("There is {:d} humanoid on the grid.")