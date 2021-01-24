class Mob:      # моб в общем, остальные мобы наследники класса Mob
    hp = int()
    damage = int()

    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

    def get_hp(self):
        return self.hp

    def get_damage(self):
        return self.damage

    def set_damage(self, damage):
        self.hp -= damage


class MobGoblin(Mob):
    hp = 25
    damage = 10

    def __init__(self):
        super().__init__(self.hp, self.damage)


class MobCrow(Mob):
    hp = 15
    damage = 20

    def __init__(self):
        super().__init__(self.hp, self.damage)


class MobSnake(Mob):        # собственно зачем реализовывал наследование, змея ядовитит дофига, похожее ещё будет
    hp = 20
    damage = 10
    poison = 5

    def __init__(self):
        super().__init__(self.hp, self.damage)

    def get_damage(self):
        self.damage += self.poison
        return self.damage


class MobLilDragon(Mob):        # огонь работает почти также как и яд, но наростает
    hp = 50
    damage = 10
    fire = 10

    def __init__(self):
        super().__init__(self.hp, self.damage)

    def get_damage(self):
        self.damage += self.fire
        self.fire += 2
        return self.damage


class MobBat(Mob):     # летучая мыш уже вомпирит дофига, то есть восстанавливает себе столько hp, сколько нанесла урона
    hp = 20
    damage = 15

    def __init__(self):
        super().__init__(self.hp, self.damage)

    def get_damage(self):
        self.hp += self.damage
        if self.hp > 100:
            self.hp = 100
        return self.damage


class MobStingray(Mob):     # а скат тупо наносит много урона он же скат лмао
    hp = 30
    damage = 45

    def __init__(self):
        super().__init__(self.hp, self.damage)
