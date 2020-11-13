import random


class Ability:
    def __init__(self, name, max_damage):
        '''
        Initialize the values passed into this method as instance variables.
        '''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage. '''
        random_value = random.randint(0, self.max_damage)
        return random_value

if __name__ == "__main__":
    ability = Ability("Debugging Ability",20)
    ability2 = Ability("smack jackie", 30)
    dmg1 = ability.attack()
    dmg2 = ability2.attack()
    print(dmg1)
    print(dmg2)
    print(dmg1 + dmg2)
   