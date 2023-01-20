from errors import PlaceError
import random

BOT = "O"
HUMAN = "X"


class RandomBot:
    """Bot making random moves for Ultimate-Tic-Tac-Toe game.

    Args:
        game (Gameplay): gameplay object.
        size (int, optional): size of the board. Defaults to 3."""
    def __init__(self, game, size=3):
        self._gameplay = game
        self._size = size

    def make_move(self):
        """Makes move on the board."""
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
    """Bot making moves for Ultimate-Tic-Tac-Toe game.
    Moves are based on the algorithm specified in documentation.

    Args:
        game (Gameplay): gameplay object.
        size (int, optional): size of the board. Defaults to 3."""
    def __init__(self, game, size=3):
        self._gameplay = game
        self._size = size
        self._board = game.game._small_boards

    def make_move(self):
        """Makes move on the board."""
        size = self._size
        squares = []
        possible_phase1 = []    # all possible fields
        possible_phase2 = []    # fields not losing board in next
        possible_phase3 = []    # fields not making all boards active in next

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

        for field in possible_phase1:
            if self.win_game(field, BOT):
                rsq, csq, rpos, cpos = field
                self._gameplay.game.make_move(rsq, csq, rpos, cpos,
                                              self._gameplay.players[0])
                self._gameplay.players.reverse()
                return None
            if self.win_board(field, BOT):
                rsq, csq, rpos, cpos = field
                self._gameplay.game.make_move(rsq, csq, rpos, cpos,
                                              self._gameplay.players[0])
                self._gameplay.players.reverse()
                return None
            if self.lose_board(field):
                possible_phase2.remove(field)
                possible_phase3.remove(field)

        for field in possible_phase2:
            if self.make_all(field):
                possible_phase3.remove(field)

        if len(possible_phase3) > 0:
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
        self._gameplay.players.reverse()

    def win_game(self, field, player):
        """Tells if game could be won by making this move."""
        if not self.win_board(field, player):
            return False

        fields = self._gameplay.game.fields
        x = field[0]
        y = field[1]
        for i in range(self._size):
            row = [player if (i == x and j == y) else fields[i][j]
                   for j in range(self._size)]
            if self.winner_state(row):
                return True

        for i in range(self._size):
            column = [player if (j == x and i == y) else fields[j][i]
                      for j in range(self._size)]
            if self.winner_state(column):
                return True

        diagonal = [player if (i == x and j == y) else fields[i][j]
                    for (i, j) in zip(range(self._size), range(self._size))]
        if self.winner_state(diagonal):
            return True
        diagonal = [player if (i == x and j == y) else fields[i][j]
                    for (i, j) in zip(range(self._size), range(self._size-1, -1, -1))]  # NOQA: E501
        if self.winner_state(diagonal):
            return True
        return False

    def win_board(self, field, player):
        """Tells if board could be won by making this move."""
        fields = self._board[field[0]][field[1]].fields
        x = field[2]
        y = field[3]
        for i in range(self._size):
            row = [player if (i == x and j == y) else fields[i][j]
                   for j in range(self._size)]
            if self.winner_state(row):
                return True

        for i in range(self._size):
            column = [player if (j == x and i == y) else fields[j][i]
                      for j in range(self._size)]
            if self.winner_state(column):
                return True

        diagonal = [player if (i == x and j == y) else fields[i][j]
                    for (i, j) in zip(range(self._size), range(self._size))]
        if self.winner_state(diagonal):
            return True
        diagonal = [player if (i == x and j == y) else fields[i][j]
                    for (i, j) in zip(range(self._size), range(self._size-1, -1, -1))]  # NOQA: E501
        if self.winner_state(diagonal):
            return True
        return False

    def lose_board(self, field):
        """Tells if board could be lost in next move by making this move.
        Called only by bot.
        """
        size = self._size
        # nojman jeśli to czytasz nie bij pls
        if self.make_all(field):
            for i in range(size):
                for j in range(size):
                    if self._board[i][j].active:
                        for x in range(size):
                            for y in range(size):
                                if (self._board[i][j].fields[x][y] is None
                                   and field != (i, j, x, y)):
                                    self.win_board(field, HUMAN)

    def make_all(self, field):
        """Tells if enemy could make move in any board by making this move.
        Called only by bot.
        """
        return not (self._gameplay.game._small_active[field[2]][field[3]])

    def winner_state(self, fields):
        """Tells whether game on this board has ended or not."""
        return (len(set(fields)) == 1 and None not in fields
                and "tie" not in fields)
