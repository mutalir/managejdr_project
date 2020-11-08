from numpy.random import choice
import yaml

class Item():
    def __init__(self, name):
        self.name = name
        with open('./item/item.yaml', 'r') as f:
            self.Items = yaml.load(f, Loader=yaml.FullLoader)
        self.caracs = self.Items[self.name]
        if self.caracs['type'] == 'Arme':
            self.caracs['damage'] = choice(self.caracs['damage']['values'], p=self.caracs['damage']['p'])