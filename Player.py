class Player:
    hp = int()
    xp = int()
    lvl = int()
    weapon = int()
    armor = int()
    inventory = []
    arts = [0]

    def __init__(self):
        self.hp = 100
        self.xp = 0
        self.lvl = 1
        self.weapon = 1
        self.armor = 101
        self.inventory.append(302)

    @staticmethod
    def lvl_up(lvl, xp):
        if xp > lvl * 100:
            xp -= lvl * 100
            lvl += 1
        return lvl, xp

    def get_hp(self):
        return self.hp

    def get_xp(self):
        return self.xp

    def get_lvl(self):
        return self.lvl

    def get_weapon(self):
        return self.weapon

    def get_armor(self):
        return self.armor

    def get_inventory(self):
        return self.inventory

    def get_arts(self):
        return self.arts

    def damage(self, damage):
        self.hp -= damage

    def plus_xp(self, xp):
        self.xp += xp
        self.lvl, self.xp = Player.lvl_up(self.lvl, self.xp)
