import random
from ability import Ability
from armor import Armor


class Hero:
    def __init__(self, name, starting_health=100):
        '''Hero class as 3 instance properties of name,
        starting health, and current health,
        armors and abilities will be empty lists '''
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        '''Current hero will take turns fighting the opponent hero passed in.
        '''
        winner = random.choice([self.name, opponent.name])
        print(f'{winner} is the winner!')

    def add_ability(self, ability):
        '''Add ability to abilities list '''
        # use append method to add ability to our list
        self.abilities.append(ability)

    def add_armor(self, armor):
        '''Add armor to armors list '''
        # use apppend method to add armor to our list
        self.armors.append(armor)

    def defend(self, damage_amt):
        ''' Calculate total block amount from all armor'''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return damage_amt - total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect damage minus the defense'''
        self.current_health -= self.defend(damage)

    def attack(self):
        ''' Calculate total attack damage amount from all abilities'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health <= 0:
            return False
        else: 
            return True
    
    def fight(self, opponent):  
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw!")
            return
        else:
            while self.is_alive() == True and opponent.is_alive() == True:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
            if self.is_alive() == True:
                print(f'{self.name} is the winner!')
            elif opponent.is_alive() == True:
                print(f'{opponent.name} is the winner!')
            else:
                print("Both died. It's a tie")

    
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)