from Player import Player
from Subjects import Subjects
import Mobs
from Loot import Loot


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


Player = Player()
Subs = Subjects()
Loot = Loot()

begins()

while True:
    command = input()
    if command == "1" or command == "Персонаж" or command == "персонаж":
        player_stats(Player)
        command = input()
        begins()
    elif command == "3" or command == "Инвентарь" or command == "инвентарь":
        inventory_stats(Player)
        command = input()
        begins()
    elif command == "4" or command == "Геномануал" or command == "геномануал":
        genomanual()
        command = input()
        begins()
    elif command == "2" or command == "Ход" or command == "ход":
        print("ну ты сходил и че")
