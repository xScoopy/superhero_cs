import random
from ability import Ability
from armor import Armor
from weapon import Weapon



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
        self.deaths = 0
        self.kills = 0

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
    
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)
        

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

    def add_kill(self, num_kills):
        ''' Update self.kills by n um_kills amount '''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths
    
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
                self.add_kill(1)
                opponent.add_death(1)
               
            elif opponent.is_alive() == True:
                print(f'{opponent.name} is the winner!')
                self.add_death(1)
                opponent.add_kill(1)
                
            else:
                print("Both died. It's a tie")
                self.add_death(1)
                self.add_kill(1)
                opponent.add_kill(1)
                opponent.add_death(1)

    
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
