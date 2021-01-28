from random import randint


class Event:
    player_luck = int()

    def create_event(self):
        event = randint(self.player_luck % 8, 10)
        if event > 8:
            return "chest"
        else:
            return "mob"

    def set_luck(self, luck):
        self.player_luck = luck
