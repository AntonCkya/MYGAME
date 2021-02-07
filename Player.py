from Subjects import Subjects


class Player:
    hp = int()
    xp = int()
    lvl = int()
    weapon = int()
    armor = int()
    inventory = []
    arts = [0]
    Subs = Subjects()
    luck = int()
    external_damage = 0

    def __init__(self):
        self.hp = 100
        self.xp = 0
        self.lvl = 1
        self.weapon = -1
        self.armor = 101
        self.inventory.append(302)
        self.inventory.append(304)
        self.luck = 0

    @staticmethod
    def lvl_up(lvl, xp):
        if xp >= lvl * 100:
            xp -= lvl * 100
            lvl += 1
        return lvl, xp

    # getters:
    def get_hp(self):
        return self.hp

    def get_xp(self):
        return self.xp

    def get_lvl(self):
        return self.lvl

    def get_weapon(self):
        return self.weapon      # id

    def get_armor(self):
        return self.armor       # id

    def get_inventory(self):
        return self.inventory       # id

    def get_arts(self):
        return self.arts        # id

    def get_luck(self):
        return self.luck

    def get_damage(self):
        return self.Subs.get_weapon_damage(self.weapon) + self.external_damage

    def get_chance(self):
        return self.Subs.get_weapon_chance(self.weapon) * self.Subs.get_armor_chance(self.armor)

    def get_external_damage(self):
        return self.external_damage

    # setters:
    def set_hp(self, hp):
        self.hp = hp

    def set_xp(self, xp):
        self.xp = xp

    def set_lvl(self, lvl):
        self.lvl = lvl

    def set_weapon(self, weapon):
        self.weapon = weapon

    def set_armor(self, armor):
        self.armor = armor

    def set_inventory(self, inventory):
        self.inventory = inventory

    def set_arts(self, arts):
        self.arts = arts

    def set_luck(self, luck):
        self.luck = luck

    def set_external_damage(self, external_damage):
        self.external_damage = external_damage

    # others:
    def plus_luck(self, l):
        self.luck += l

    def damage(self, damage):
        self.hp -= damage

    def plus_xp(self, xp):
        self.xp += xp
        self.lvl, self.xp = Player.lvl_up(self.lvl, self.xp)

    def heal(self, hp):
        self.hp += hp

    def remove_from_inventory(self, item):
        self.inventory.pop(item)

    def plus_damage(self, dmg):
        self.external_damage += dmg
