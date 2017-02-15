import random

class Character(object):
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def __repr__(self):
        return "%s" % self.name

    def attack(self, other_character):
        other_character.health -= self.power
        print "%s does %d damage to the %s." % (self.name,
        self.power, other_character)
        if other_character.health <= 0:
            print "%s is dead." % other_character

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health,
        self.power)

class Hero(Character):
    def __init__(self, name):
        self.health = 10
        self.power = 5
        self.name = name

    def attack(self, other_character):
        if random.randint(1, 5) == 3: #doubles hero's power with 20% probability
            self.power = self.power * 2
        else:
            pass
        other_character.health -= self.power
        print "%s does %d damage to the %s." % (self.name,
        self.power, other_character)
        if other_character.health <= 0:
            print "%s is dead." % other_character

class Goblin(Character):
    def __init__(self, name):
        self.health = 6
        self.power = 2
        self.name = name

class Zombie(Character):
    def __init__(self, name):
        self.health = hero.health + 1
        self.power = 5
        self.name = name

hero = Hero("steve the hero")
goblin = Goblin("jerry the goblin")
zombie = Zombie("tommy the zombie")

####CLASSES ABOVE####

def main():

    while zombie.alive() and hero.alive():
        hero.print_status()
        zombie.print_status()
        print "What do you want to do?"
        print "1. fight zombie"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            hero.attack(zombie)
        elif input == "2":
            zombie.attack(hero)
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input


main()
