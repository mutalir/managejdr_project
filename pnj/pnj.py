from item.item import Item
from numpy.random import choice, randint
import yaml
from collections import OrderedDict as OD


class Pnj():
    def __init__(self, type):
        self.type = type
        with open("./pnj/caracs.yaml", 'r', encoding='utf-8') as f:
            self.Caracs = yaml.load(f, Loader=yaml.FullLoader)
        self.name = choice(self.Caracs[self.type]['prénom']) + ' ' + choice(self.Caracs[self.type]['nom'])  #Faire en sorte qu'il n'y ait pas le même nom
        self.vie = randint(self.Caracs[self.type]["vie"]['min'], self.Caracs[self.type]["vie"]['max'])
        self.force = randint(self.Caracs[self.type]["force"]['min'], self.Caracs[self.type]["force"]['max'])
        self.endurance = randint(self.Caracs[self.type]["endurance"]['min'], self.Caracs[self.type]["endurance"]['max'])
        self.dexterite = randint(self.Caracs[self.type]["dextérité"]['min'], self.Caracs[self.type]["dextérité"]['max'])
        self.perception = randint(self.Caracs[self.type]["perception"]['min'], self.Caracs[self.type]["perception"]['max'])
        self.savoir = randint(self.Caracs[self.type]["savoir"]['min'], self.Caracs[self.type]["savoir"]['max'])
        self.santementale = randint(self.Caracs[self.type]["santé mentale"]['min'], self.Caracs[self.type]["santé mentale"]['max'])
        self.pouvoir = randint(self.Caracs[self.type]["pouvoir"]['min'], self.Caracs[self.type]["pouvoir"]['max'])
        self.discretion = randint(self.Caracs[self.type]["discrétion"]['min'], self.Caracs[self.type]["discrétion"]['max'])
        self.charisme = randint(self.Caracs[self.type]["charisme"]['min'], self.Caracs[self.type]["charisme"]['max'])
        self.pilotage = randint(self.Caracs[self.type]["pilotage"]['min'], self.Caracs[self.type]["pilotage"]['max'])
        self.artisanat = randint(self.Caracs[self.type]["artisanat"]['min'], self.Caracs[self.type]["artisanat"]['max'])
        self.items = self.Caracs[self.type]['loot']

        self.equipement = {}

        self.loot = {}

    def Equiper(self):
        for it in self.items:
            n = randint(1, 100)
            if n < self.items[it]:
                item = Item(it)
                self.equipement[it] = item

    def Looter(self):
        return self.equipement

    def AfficherCaracs(self):
        d = OD([('Nom', self.name), ('Vie', self.vie), ('Force', self.force), ('Endurance', self.endurance),
             ('Dextérité', self.dexterite), ('Perception', self.perception), ('Savoir', self.savoir),
             ('Santé mentale', self.santementale), ('Pouvoir', self.pouvoir), ('Discrétion', self.discretion),
             ('Charisme', self.charisme), ('Pilotage', self.pilotage), ('Artisanat', self.artisanat),
             ('Équipement', self.equipement)])
        return d
