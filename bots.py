from errors import PlaceError
import random


class RandomBot:
    """Bot making random moves for Ultimate-Tic-Tac-Toe game
    Arguments:
    game:   gameplay object with players and access to board methods
    size:   (default=3) size of the board"""
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
    """Bot making moves for Ultimate-Tic-Tac-Toe game based on algorithm
    Arguments:
    game:   gameplay object with players and access to board methods
    size:   (default=3) size of the board"""
    def __init__(self, game, size=3):
        self._gameplay = game
        self._size = size
        self._board = game.game._small_boards

    def make_move(self):
        size = self._size
        squares = []
        possible_phase1 = []    # all possible fields
        possible_phase2 = []    # fields not losing game in next
        possible_phase3 = []    # fields not losing board in next
        possible_phase4 = []    # fields not making all boards active in next

        # adding all active fields to possible fields
        if self._gameplay.game.which_active() == "all":
            for i in range(size):
                for j in range(size):
                    squares.append((i, j))
        else:
            squares.append(self._gameplay.game.which_active())
        for i in range(size):
            for j in range(size):
                if (i, j) in squares and self._board[i][j].active:
                    for x in range(size):
                        for y in range(size):
                            if self._board[i][j].fields[x][y] is None:
                                possible_phase1.append((i, j, x, y))
                                possible_phase2.append((i, j, x, y))
                                possible_phase3.append((i, j, x, y))
                                possible_phase4.append((i, j, x, y))

        for field in possible_phase1:
            if self.win_game(field):
                rsq, csq, rpos, cpos = field
                self._gameplay.game.make_move(rsq, csq, rpos, cpos,
                                              self._gameplay.players[0])
                return None
            if self.lose_game(field):
                possible_phase2.remove(field)
                possible_phase3.remove(field)
                possible_phase4.remove(field)

        for field in possible_phase2:
            if self.win_board(field):
                rsq, csq, rpos, cpos = field
                self._gameplay.game.make_move(rsq, csq, rpos, cpos,
                                              self._gameplay.players[0])
                return None
            if self.lose_board(field):
                possible_phase3.remove(field)
                possible_phase4.remove(field)

        for field in possible_phase3:
            if self.make_all(field):
                possible_phase4.remove(field)

        if len(possible_phase4) > 0:
            rsq, csq, rpos, cpos = random.choice(possible_phase4)
            self._gameplay.game.make_move(rsq, csq, rpos, cpos,
                                          self._gameplay.players[0])
        elif len(possible_phase3) > 0:
            rsq, csq, rpos, cpos = random.choice(possible_phase3)
            self._gameplay.game.make_move(rsq, csq, rpos, cpos,
                                          self._gameplay.players[0])
        elif len(possible_phase2) > 0:
            rsq, csq, rpos, cpos = random.choice(possible_phase2)
            self._gameplay.game.make_move(rsq, csq, rpos, cpos,
                                          self._gameplay.players[0])
        else:
            rsq, csq, rpos, cpos = random.choice(possible_phase1)
            self._gameplay.game.make_move(rsq, csq, rpos, cpos,
                                          self._gameplay.players[0])

    def win_game(self, field):
        pass

    def lose_game(self, field):
        pass

    def win_board(self, field):
        pass

    def lose_board(self, field):
        pass

    def make_all(self, field):
        pass
