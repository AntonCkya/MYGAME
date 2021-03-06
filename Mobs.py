from random import randint


class Mob:      # моб в общем, остальные мобы наследники класса Mob
    hp = int()
    damage = int()
    rank = int()

    def __init__(self, hp, damage, rank):
        self.hp = hp
        self.damage = damage
        self.rank = rank

    def get_hp(self):
        return self.hp

    def get_damage(self):
        return self.damage

    def get_rank(self):
        return self.rank

    def set_damage(self, damage):
        self.hp -= damage


class MobGenerator:
    tier_list = ["Goblin", "Crow", "Snake", "Lil Dragon", "Bat", "Stingray", "Spider", "Turtle"]
    player_lvl = int()

    def set_player_lvl(self, lvl):
        self.player_lvl = lvl

    def get_mob(self):
        mob = randint(1, self.player_lvl * 2)
        return self.tier_list[mob - 1]


class MobGoblin(Mob):
    hp = 25
    damage = 10
    rank = 1

    def __init__(self):
        super().__init__(self.hp, self.damage, self.rank)


class MobCrow(Mob):
    hp = 15
    damage = 20
    rank = 1

    def __init__(self):
        super().__init__(self.hp, self.damage, self.rank)


class MobSnake(Mob):        # собственно зачем реализовывал наследование, змея ядовитит дофига, похожее ещё будет
    hp = 20
    damage = 10
    rank = 2
    poison = 5

    def __init__(self):
        super().__init__(self.hp, self.damage, self.rank)

    def get_damage(self):
        self.damage += self.poison
        return self.damage


class MobLilDragon(Mob):        # огонь работает почти также как и яд, но наростает
    hp = 50
    damage = 10
    fire = 10
    rank = 2

    def __init__(self):
        super().__init__(self.hp, self.damage, self.rank)

    def get_damage(self):
        self.damage += self.fire
        self.fire += 2
        return self.damage


class MobBat(Mob):     # летучая мыш уже вомпирит дофига, то есть восстанавливает себе столько hp, сколько нанесла урона
    hp = 20
    damage = 15
    rank = 3

    def __init__(self):
        super().__init__(self.hp, self.damage, self.rank)

    def get_damage(self):
        self.hp += self.damage
        if self.hp > 100:
            self.hp = 100
        return self.damage


class MobStingray(Mob):     # а скат тупо наносит много урона он же скат лмао
    hp = 30
    damage = 45
    rank = 3

    def __init__(self):
        super().__init__(self.hp, self.damage, self.rank)


class MobSpider(Mob):       # почти как змея, но от яда урон растёт сильнее, при этом 1 удар наносит ничтожные 5 урона
    hp = 30                 # также немного регенится во время хода
    damage = -20
    poison = 25
    regeneration = 0
    rank = 4

    def __init__(self):
        super().__init__(self.hp, self.damage, self.rank)

    def get_damage(self):
        self.damage += self.poison
        self.hp += self.regeneration
        self.regeneration += 5
        return self.damage


class MobTurtle(Mob):       # черепаха с каждым ударом по ней принимает меньше урона
    hp = 50                 # наверное это можно будет сломать но мне пофиг
    damage = 10
    defence = 1
    rank = 4

    def __init__(self):
        super().__init__(self.hp, self.damage, self.rank)

    def set_damage(self, damage):
        started_hp = self.hp
        self.hp -= damage
        self.hp += self.defence
        self.defence += 3
        if self.hp >= started_hp:
            self.hp = started_hp - 1
