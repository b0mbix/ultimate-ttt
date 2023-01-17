class SizeError(Exception):
    pass


class Board:
    """
    A sizeXsize board, a parent for SmallBoard and BigBoard classes.
    Optional arguments:
    size:   odd integer not less than 3, width and height of the board.
    """

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
            if (len(set(fields)) == 1 and None not in fields
                    and "tie" not in fields):
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
    """
    A sizeXsize big board.
    Contains both final fields and small boards with information about them.
    Optional arguments:
    size:   odd integer not less than 3, width and height of the board.
    """
    def __init__(self, size=3):
        super().__init__(size)
        self._small_boards = []
        self._small_active = []
        for i in range(size):
            self._small_boards.append([])
            self._small_active.append([])
            for _ in range(size):
                self._small_boards[i].append(SmallBoard(self, size))
                self._small_active[i].append(True)

    def make_move(self, board_x, board_y, x, y, player):
        board_active = self._small_active[board_x][board_y]
        board = self._small_boards[board_x][board_y]
        if self._active and board_active:
            if board.make_move(x, y, player):
                self.fields[board_x][board_y] = self.board.check_winner(x, y)
                self.check_winner(x, y)
                self.activate_boards(x, y)

    def activate_boards(self, x, y):
        if self._small_boards[x][y].active is True:
            for i in range(self._size):
                for j in range(self._size):
                    self._small_active[i][j] = False
            self._small_active[x][y] = True
        else:
            for i in range(self._size):
                for j in range(self._size):
                    self._small_active[i][j] = True


class SmallBoard(Board):
    """
    A sizeXsize small board.
    Basically default board, but returns information if move was successful.
    Optional arguments:
    size:   odd integer not less than 3, width and height of the board.
    """
    def __init__(self, big, size=3):
        super().__init__(size)
        self._big_board = big

    def make_move(self, x, y, player):
        if not (self._active and self.fields[x][y] is None):
            return False
        self.fields[x][y] = player
        self.check_winner()
        return True
