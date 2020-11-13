import random

class Hero:
    def __init__(self, name, starting_health=100):
        '''Hero class as 3 instance properties of name, 
        starting health, and current health '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        '''Current hero will take turns fighting the opponent hero passed in.
        '''
        winner = random.choice([self.name, opponent.name])
        print(f'{winner} is the winner!')
if __name__ == "__main__":
    #If you run this file from the terminal
    #this block is executed
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)
