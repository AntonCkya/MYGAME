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
    for i in inventory:
        print(Subs.get_item(i))
    print("Любая команда для возврата назад...")


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


Player = Player()
Subs = Subjects()
Loot = Loot()
Event = Event()
MobGenerator = Mobs.MobGenerator()

begins()

while True:
    command = input()
    if command == "1":
        player_stats(Player)
        command = input()
        begins()
    elif command == "3":
        inventory_stats(Player)
        command = input()
        begins()
    elif command == "4":
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
            while fight:
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
            print("Бой окончен, введите любую команду...")
            Player.set_hp(100)
            print("Здоровье восстановлено до 100, пока не придуман инвентарь с хиллками")
            command = input()
            begins()
