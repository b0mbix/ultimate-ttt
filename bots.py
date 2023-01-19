from errors import PlaceError
import random


class RandomBot:
    def __init__(self, game, size=3):
        self._gameplay = game
        self._size = size

    def make_move(self):
        size = self._size
        if self._gameplay.game.which_active() == "all":
            rsq = random.randint(0, size-1)
            csq = random.randint(0, size-1)
        else:
            rsq, csq = self._gameplay.game.which_active()
        rpos = random.randint(0, size-1)
        cpos = random.randint(0, size-1)
        try:
            self._gameplay.game.make_move(rsq, csq, rpos, cpos,
                                          self._gameplay.players[0])
            self._gameplay.players.reverse()
        except PlaceError:
            self.make_move()


class SmartBot:
    pass
