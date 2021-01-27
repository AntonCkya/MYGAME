class Subjects:
    subjects = {
        -1: "Fork",
        1: "Katana",
        2: "Nail",
        3: "Axe",
        4: "Hammer",
        5: "Awl",
        101: "Cloak",
        102: "Jacket",
        103: "Chain-mail",
        201: "Sharpening kit",  # +5 к урону
        202: "Golden apple",    # +25 hp
        203: "Self-instruction book",   # *1.1 xp
        204: "Drug making kit",     # *1.5 восстановления hp, при снятии ломается
        205: "Rotten foot",     # +5 удачи, при снятии ломается
        206: "Heavy belt",      # +1 слот под артифакт, -3 урон
        301: "Aid kit",     # +50 отхилл
        302: "Apple",   # +10 отхилл, +5 удачи на 3 хода
        303: "Toxic fish",    # -5 отхилл за каждый ход, на 5 ходов; +10 урон на 5 ходов
        304: "Sake"     # первые 5 ходов: +15 hp, +5 урон; последующие 10 ходов: -10 hp, -10 удача
    }
    weapon = {      # ( урон, шанс атаки )
        -1: (10, 0.5),
        1: (20, 0.5),
        2: (5, 0.8),
        3: (25, 0.45),
        4: (40, 0.3),
        5: (15, 0.8)
    }
    armor = {       # ( дополнительное hp, градация шанса )
        101: (0, 1),
        102: (5, 1),
        103: (15, 0.9)
    }

    def get_item(self, item):
        return self.subjects[item]

    def get_weapon_damage(self, i):
        return self.weapon[i[0]]

    def get_weapon_chance(self, i):
        return self.weapon[i[1]]

    def get_armor_hp(self, i):
        return self.armor[i[0]]

    def get_armor_chance(self, i):
        return self.armor[i[1]]

    def get_all_subjects(self):
        return self.subjects.items()
