"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to
the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power, self.armor, self.evade)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health,
        self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'Gyro the hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evade = 0

    def attack(self, enemy):
        if random.randint(1, 5) == 3: #doubles hero's power with 20% probability
             enemy.receive_damage(self.power * 2)
        else:
            pass
        enemy.receive_damage(self.power)
        time.sleep(1.5)

#ARMOR COMPONENT IS PART OF THIS BELOW (NEED TO COMPLETE EVADE COMPONENT)
    def receive_damage(self, points, armor, evade):
        updated_points = (points - self.armor)
        if self.evade > 0:
            evasion_prob = self.evade * #left off here
            if updated_points > 0:
                self.health -= updated_points
                print "%s received %d damage." % (self.name, updated_points)
            else:
                print "%s received 0 damage, weak!" % (self.name)
        elif updated_points > 0:
            self.health -= updated_points
            print "%s received %d damage." % (self.name, updated_points)
        else:
            print "%s received 0 damage, weak!" % (self.name)
        if self.health <= 0:
            print "%s is dead." % self.name

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def bounty(self, enemy):
        self.coins += enemy.coins
        print "%s received a bounty of %d coins!" % (self.name, enemy.coins)

    def print_status(self):
        print "%s has %d health, %d power, and %d armor." % (self.name, self.health,
        self.power, self.armor)

class Goblin(Character):
    def __init__(self):
        self.name = 'Bob the goblin'
        self.health = 6
        self.power = 2
        self.coins = 5
        self.armor = 0
        self.evade = 0

class Wizard(Character):
    def __init__(self):
        self.name = 'Woody the wizard'
        self.health = 8
        self.power = 1
        self.coins = 6
        self.armor = 0
        self.evade = 0

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name,
            enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self):
        self.name = 'Epidemic the medic'
        self.health = 8
        self.power = 2
        self.armor = 0
        self.evade = 0

    def receive_damage(self, points):#adds 2 points to Medic's health with 20% probability
        self.health -= points
        if random.randint(1, 5) == 3:
            self.health += 2
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

class Shadow(Character):
    def __init__(self):
        self.name = 'Shady the shadow'
        self.health = 1
        self.power = 2
        self.armor = 0
        self.evade = 0

    def receive_damage(self, points):#allows character to receive damage 10% of
                                     #the time
        if random.randint(1, 10) == 5:
            self.health -= points
            print "%s received %d damage." % (self.name, points)
        else:
            print "%s avoided the attack!" % self.name
        if self.health <= 0:
            print "%s is dead." % self.name

class Zombie(Character):
    def __init__(self):
        self.name = 'Fred the zombie'
        self.health = 0
        self.power = 5
        self.armor = 0
        self.evade = 0

    def alive(self):
        return True

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health == 0:
            print "%s can't die, muahahaha!" % self.name

class Spicey(Character):
    def __init__(self):
        self.name = 'Spicey the spox'
        self.health = 8
        self.power = 2
        self.spicey_health = 100000
        self.spicey_power = 100000
        self.armor = 0
        self.evade = 0

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.spicey_health,
        self.spicey_power)
        self.spicey_health = self.spicey_health * 100000
        self.spicey_power = self.spicey_power * 100000

class Kellyanne(Character):
    def __init__(self):
        self.name = 'Kellyanne'
        self.health = 8
        self.power = 1
        self.armor = 0
        self.evade = 0

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health,
        self.power)
        if self.health == 8:
            print """Kellyanne says: Have you been to the store yet? You should
really go buy some of the Bob the Goblin's swords in the store. The swords are
great products. I'm using one of his swords right now."""
        elif self.health < 8:
            print """Kellyanne says: Have you checked out Bob's tonics yet?"""

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Gyro the hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated %s" % enemy.name
            hero.bounty(enemy)
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, hero):
        hero.health += 2
        print "%s's health increased to %d." % (hero.name, hero.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class SuperTonic(object):
    cost = 5
    name = 'supertonic'
    def apply(self, hero):
        hero.health = 10
        print "%s's armor increased to %d." % (hero.name, hero.health)

class Armor(object):
    cost = 5
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2
        print "%s's armor increased to %d." % (hero.name, hero.armor)

class Evasion(object):
        cost = 2
        name = 'evasion'
        def apply(self, hero):
            hero.evade += 2
            print "%s's evasion increased to %d." % (hero.name, hero.evade)

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, Armor, Evasion]
    def do_shopping(self, hero):
        while True:
            if hero.coins <= 0:
                print "====================="
                print "Sorry, you're all out of coins!"
                break
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            elif input > (len(Store.items)):
                print "No such product exists in our inventory!"
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                if item.cost > hero.coins:
                    print "You can't afford that!"
                else:
                    hero.buy(item)

hero = Hero()
enemies = [Goblin(), Wizard(), Zombie(), Shadow(), Medic(), Spicey(), Kellyanne()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
