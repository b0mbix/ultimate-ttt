from errors import SizeError, RangeError, ActiveError, PlaceError


class Board:
    """
    A sizeXsize board, a parent for SmallBoard and BigBoard classes.

    Args:
            size (int, optional): size of the board. Defaults to 3.
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
        """Property returning value of self._active."""
        return self._active

    def make_move(self, x, y, player):
        if self._active and self.fields[x][y] is None:
            self.fields[x][y] = player
            self.check_winner()

    def check_winner(self):
        """Returns information who won this board;
        returns None if game hasn't ended yet"""
        def winner_state(fields):
            """Tells whether game on this board has ended or not."""
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

    Args:
            size (int, optional): _description_. Defaults to 3.
    """
    def __init__(self, size=3):
        super().__init__(size)
        self.small_boards = []
        self._small_active = []
        for i in range(size):
            self.small_boards.append([])
            self._small_active.append([])
            for _ in range(size):
                self.small_boards[i].append(SmallBoard(size))
                self._small_active[i].append(True)

    def make_move(self, board_x, board_y, x, y, player):
        """Processes move making on a board;
        sends make move information to SmallBoard object,
        adds player move on big board if game on small board has ended.
        """
        size = self._size
        if (board_x not in range(size) or board_y not in range(size)
           or x not in range(size) or y not in range(size)):
            raise RangeError("Incorrect arguments")
        board_active = self._small_active[board_x][board_y]
        board = self.small_boards[board_x][board_y]
        if not (self._active and board_active):
            raise ActiveError("This board is not active")
        if not board.make_move(x, y, player):
            raise PlaceError("This place is already occupied")
        self.fields[board_x][board_y] = board.check_winner()
        self.check_winner()
        self.activate_boards(x, y)

    def activate_boards(self, x, y):
        """Activates boards based on previous move."""
        if self.small_boards[x][y].active is True:
            for i in range(self._size):
                for j in range(self._size):
                    self._small_active[i][j] = False
            self._small_active[x][y] = True
        else:
            for i in range(self._size):
                for j in range(self._size):
                    self._small_active[i][j] = True

    def get_small_value(self, sx, sy, x, y):
        """Gets value of a field on a small board."""
        return self.small_boards[sx][sy].fields[x][y]

    def which_active(self):
        """Returns information about active boards (includes finished boards).
        """
        count = 0
        x = 0
        y = 0
        for i in range(self._size):
            for j in range(self._size):
                if self._small_active[i][j]:
                    count += 1
                    x = i
                    y = j
                if count > 1:
                    return "all"
        return (x, y)


class SmallBoard(Board):
    """
    A sizeXsize small board inheriting from Board class.
    Basically default board, but returns information if move was successful.

    Args:
            size (int, optional): Size of the board. Defaults to 3.
    """
    def __init__(self, size=3):
        super().__init__(size)

    def make_move(self, x, y, player):
        """Makes move on small board;
        returns information if move was successful.
        """
        if not (self._active and self.fields[x][y] is None):
            return False
        self.fields[x][y] = player
        self.check_winner()
        return True
