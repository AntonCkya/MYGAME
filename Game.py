from Player import Player
from Subjects import Subjects
import Mobs
from Loot import Loot
from Event import Event
from random import randint

"""
HP - здоровье ( если становится ниже 0 персонаж умирает )
XP - опыт ( получается от убийства врагов )
LVL - уровень героя ( чем выше уровень, тем выше HP, XP, Damage )
Damage - урон героя ( в бою умножается от 0.75 до 1.25 в зависимости от рандома )
Chance - шанс атаки ( является произведением шанса от оружия, от брони и аксессуаров)
Luck - удача ( от неё зависит качество выпадаемых предметов )
*****
Некоторые артефакты дают особенные параметры, такие как дополнительный процент к восстановлению здоровья препаратами или
    дополнительные слоты для артефактов
Некоторые артефакты при снятии ломаются
*****
Аксы реализовывать пока небуду ибо впадлу
"""


def begins():
    print("Команды:")
    print("1:Персонаж")
    print("2:Ход")
    print("3:Инвентарь")
    print("4:Геномануал")


def player_stats(player):
    print("HP:", player.get_hp())
    print("XP: " + str(player.get_xp()) + "/" + str(player.get_lvl() * 100))
    print("LVL:", player.get_lvl())
    print("Любая команда для возврата назад...")


def inventory_stats(player):
    inventory = player.get_inventory()
    print("Инвентарь персонажа:")
    for i in enumerate(inventory):
        print(i[0] + 1, ": ", end="")
        print(Subs.get_item(i[1]))
    print("Введите номер предмета, чтобы его использовать, или 0, чтобы выйти в меню")
    return len(inventory)


def genomanual():
    manual = Subs.get_all_subjects()
    print("Геномануал всех игровых предметов:")
    for i in manual:
        print(*i)
    print("Любая команда для возврата назад...")


def fight_stats(player, mob):
    print("Твоё HP:", player.get_hp())
    print("HP Врага:", mob.get_hp())
    print("Команды:")
    print("1:Атака")
    print("2:Инвентарь")


def fight_player_attack(player):
    print("Вы аттакуете:")
    damage = player.get_damage()
    chance = player.get_chance() * 100
    if chance < randint(1, 100):
        return 0
    else:
        return damage


def fight_mob_attack(mob):
    print("Моб аттакует:")
    damage = mob.get_damage()
    return damage


def use(num_item, player):
    id_item = player.get_inventory()[num_item - 1]
    player.remove_from_inventory(num_item - 1)
    if id_item == 301:
        print("Лави оптечку")
        player.heal(50)
    elif id_item == 302:  # Пока градации по ходам нет ну я тупой че
        print("Зато не андроид")
        player.heal(10)
        player.plus_luck(5)
    elif id_item == 303:
        print("Ну ты и токсик")
        print(None)
    elif id_item == 304:
        print("Эта,.. чтоб руки не дрожали...")
        player.heal(15)
        player.plus_damage(5)


Player = Player()
Subs = Subjects()
Loot = Loot()
Event = Event()
MobGenerator = Mobs.MobGenerator()

begins()
acts = 0

while True:
    command = input()
    if command == "1":
        player_stats(Player)
        command = input()
        begins()
    elif command == "3":
        inventory_size = inventory_stats(Player)
        command = input()
        if 0 < int(command) <= inventory_size:
            acts += 1
            use(int(command), Player)
        begins()

    elif command == "4":
        acts += 1
        genomanual()
        command = input()
        begins()
    elif command == "2":
        Event.set_luck(Player.get_luck())
        event = Event.create_event()
        if event == "mob":
            print("У вас на пути моб, а именно:")
            fight = True
            MobGenerator.set_player_lvl(Player.get_lvl())
            mob = MobGenerator.get_mob()
            print(mob)
            Mob = Mobs.Mob(0, 0, 0)
            if mob == "Goblin":
                Mob = Mobs.MobGoblin()
            elif mob == "Crow":
                Mob = Mobs.MobCrow()
            # Сделай ещё мобов тута
            while fight:
                acts += 1
                fight_stats(Player, Mob)
                command = input()
                if command == "1":
                    damage = fight_player_attack(Player)
                    if damage == 0:
                        print("Неповезло, ты не аттакуешь")
                    else:
                        print("Вы наносите " + str(damage) + " урона")
                        Mob.set_damage(damage)
                    if Mob.get_hp() <= 0:
                        print("Моб был убит")
                        xp = Mob.get_rank() * 50
                        print("Получено XP:", xp)
                        Player.plus_xp(xp)
                        fight = False
                    else:
                        print("Здоровье моба:", Mob.get_hp())
                        damage = fight_mob_attack(Mob)
                        print("Моб наносит " + str(damage) + " урона")
                        Player.damage(damage)
                        print("Ваше здоровье:", Player.get_hp())
                else:
                    inventory_size = inventory_stats(Player)
                    command = input()
                    if 0 < int(command) <= inventory_size:
                        acts += 1
                        use(int(command), Player)
            print("Бой окончен, введите любую команду...")
            command = input()
            begins()
        if event == "chest":
            print(None)
            # Сделай сундуки
