from random import randint
from Subjects import Subjects

'''
Антоха, пожалуйста, реализуй удачу в классе Player
Я не могу наормльно реализовать Лут-генератор из-за этого
Даю тебе неделю
'''


class Loot:
    generator = int()
    Subs = Subjects()
    luck = int()

    def generate_item(self, luck):
        self.luck = luck
        self.generator = randint(1, 20 - randint(0, luck))
        if self.generator == 1:
            return Loot.generate_armor()
        elif 1 < self.generator < 5:
            return Loot.generate_weapon()
        elif 6 < self.generator < 9:
            return Loot.generate_art()
        else:
            return Loot.generate_consumable()

    @staticmethod
    def generate_weapon():
        generator = randint(1, 5)
        return generator

    @staticmethod
    def generate_armor():
        generator = randint(1, 3)
        return generator

    @staticmethod
    def generate_art():
        generator = randint(1, 6)
        return generator

    @staticmethod
    def generate_consumable():
        generator = randint(1, 4)
        return generator
