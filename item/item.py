from numpy.random import choice
import yaml

class Item():
    def __init__(self, name):
        self.name = name
        with open('./item/item.yaml', 'r', encoding='utf-8') as f:
            self.Items = yaml.load(f, Loader=yaml.FullLoader)
        self.caracs = self.Items[self.name]
        if self.caracs['type'] == 'Arme':
            self.caracs['dommage'] = choice(self.caracs['dommage']['values'], p=self.caracs['dommage']['p'])