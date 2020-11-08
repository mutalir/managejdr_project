from item.item import Item
from numpy.random import choice, randint
import yaml
from collections import OrderedDict as OD


class Pnj():
    def __init__(self, type):
        self.type = type
        with open("./pnj/caracs.yaml", 'r') as f:
            self.Caracs = yaml.load(f, Loader=yaml.FullLoader)
        self.name = choice(self.Caracs[self.type]['name'])   #Faire en sorte qu'il n'y ait pas le même nom
        self.life = randint(self.Caracs[self.type]["life"]['min'], self.Caracs[self.type]["life"]['max'])
        self.strength = randint(self.Caracs[self.type]["strength"]['min'], self.Caracs[self.type]["strength"]['max'])
        self.stamina = randint(self.Caracs[self.type]["stamina"]['min'], self.Caracs[self.type]["stamina"]['max'])
        self.dexterity = randint(self.Caracs[self.type]["dexterity"]['min'], self.Caracs[self.type]["dexterity"]['max'])
        self.perception = randint(self.Caracs[self.type]["perception"]['min'], self.Caracs[self.type]["perception"]['max'])
        self.knowledge = randint(self.Caracs[self.type]["knowledge"]['min'], self.Caracs[self.type]["knowledge"]['max'])
        self.sanity = randint(self.Caracs[self.type]["sanity"]['min'], self.Caracs[self.type]["sanity"]['max'])
        self.power = randint(self.Caracs[self.type]["power"]['min'], self.Caracs[self.type]["power"]['max'])
        self.stealth = randint(self.Caracs[self.type]["stealth"]['min'], self.Caracs[self.type]["stealth"]['max'])
        self.charisma = randint(self.Caracs[self.type]["charisma"]['min'], self.Caracs[self.type]["charisma"]['max'])
        self.steering = randint(self.Caracs[self.type]["steering"]['min'], self.Caracs[self.type]["steering"]['max'])
        self.craft = randint(self.Caracs[self.type]["craft"]['min'], self.Caracs[self.type]["craft"]['max'])
        self.items = self.Caracs[self.type]['loot']

        self.equipment = {}

        self.loot = {}

    def Equip(self):
        for it in self.items:
            n = randint(1, 100)
            if n < self.items[it]:
                item = Item(it)
                self.equipment[it] = item

    def Loot(self):
        return self.equipment

    def DisplayCaracs(self):
        d = OD([('Nom', self.name), ('Vie', self.life), ('Force', self.strength), ('Endurance', self.stamina),
             ('Dextérité', self.dexterity), ('Perception', self.perception), ('Savoir', self.knowledge),
             ('Santé mentale', self.sanity), ('Pouvoir', self.power), ('Discrétion', self.stealth),
             ('Charisme', self.charisma), ('Pilotage', self.steering), ('Artisanat', self.craft),
             ('Équipement', self.equipment)])
        return d
