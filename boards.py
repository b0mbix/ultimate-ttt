class SizeError(Exception):
    pass


class Board:
    """A sizeXsize board.
        Values of fields: None or Player object"""

    def __init__(self, size=3):
        self._active = True
        self._size = size
        self.fields = []

        if size < 3 or size % 2 == 0:
            raise SizeError("Size has to be an odd number greater than one")

        # creating board fields
        for i in range(size):
            self.fields.append([])
            for _ in range(size):
                self.fields[i].append(None)

    @property
    def active(self):
        return self._active

    def set_active(self, state):
        if self.check_winner() is None:
            self._active = state
        else:
            self._active = False

    def make_move(self, x, y, player):
        if self._active and self.fields[x][y] is None:
            self.fields[x][y] = player
            self.check_winner()

    def check_winner(self):
        def winner_state(fields):
            if len(set(fields)) == 1 and None not in fields:
                self._active = False
                return True
            return False

        for row in self.fields:
            if winner_state(row):
                return row[0]

        for i in range(self._size):
            column = [self.fields[j][i] for j in range(self._size)]
            if winner_state(column):
                return column[0]

        diagonal = [self.fields[i][j] for (i, j)
                    in zip(range(self._size), range(self._size))]
        if winner_state(diagonal):
            return diagonal[0]
        diagonal = [self.fields[i][j] for (i, j)
                    in zip(range(self._size), range(self._size-1, -1, -1))]
        if winner_state(diagonal):
            return diagonal[0]

        for row in self.fields:
            for field in row:
                if field is None:
                    return None

        self._active = False
        return "tie"


class BigBoard(Board):
    pass


class SmallBoard(Board):
    pass
