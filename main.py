from boards import BigBoard
from errors import SizeError, RangeError, ActiveError, PlaceError, ModeError
import os


FIELDS_EMPTY = "[ ]"
FIELDS_X = "[X]"
FIELDS_O = "[O]"


def clear():
    os.system("clear")


class Game:
    """Class responsible for game and interface"""
    def __init__(self):
        self._players = ['X', 'O']
        clear()
        print("Welcome to Ultimate Tic-Tac-Toe!\n")
        self.get_size()
        self.get_mode()
        while self._game.active:
            self.next_move()
        self.generate_board()
        self.generate_endgame()

    def next_move(self):
        self.generate_board()
        self.generate_active()
        print(f"{self._players[0]} move!")
        try:
            rsq = int(input("Enter row square (first number in rows): "))-1
            csq = int(input("Enter column square (first number in columns): "))-1       # noqa: E501
            rpos = int(input("Enter row position (second number in rows): "))-1
            cpos = int(input("Enter column position (second number in columns): "))-1     # noqa: E501
        except ValueError:
            print("You have to give a number!")
            input("Press Enter to continue...")
            return None
        try:
            if self._game.make_move(rsq, csq, rpos, cpos, self._players[0]):
                self._players.reverse()
        except RangeError:
            print("Incorrect move, one or more values are out of range.")
            input("Press Enter to continue...")
        except ActiveError:
            print("This board is not active.")
            input("Press Enter to continue...")
        except PlaceError:
            print("This place is already taken.")
            input("Press Enter to continue...")

    def get_size(self, next_time=0):
        if not next_time:
            print("Default board size is 3, other sizes are not recommended.")
        try:
            self._size = int(input("Enter board size: "))
            self._game = BigBoard(self._size)
        except SizeError:
            print("Incorrect board size!")
            print("Mind that size has to be and odd number not less than 3.")
            self.get_size(1)
        except ValueError:
            print("You have to give a number.")
            self.get_size(1)

    def get_mode(self, next_time=0):
        if not next_time:
            print("Available modes:")
            print("1. Player vs Player")
            print("2. Player vs random AI (not available yet)")
            print('3. Player vs "smart" AI (not available yet)')
        possible = [1]
        try:
            mode = int(input("Enter mode: "))
            if mode not in possible:
                raise ModeError
        except ModeError:
            print("Incorrect mode!")
            self.get_mode(1)
        except ValueError:
            print("You have to give a number.")
            self.get_mode(1)

    def generate_board(self):
        size = self._size
        clear()
        print("   ", end="")
        for i in range(1, size+1):
            for j in range(1, size+1):
                print(f"   {i}.{j}", end="")
            print("    ", end="")
        print()
        for i in range(1, size+1):
            for j in range(1, size+1):
                self.generate_row(i, j)
                print()
            if size-i:
                print("      "+'-'*(6*size**2+size-1+3*(size-2)))
        print("\n")

    def generate_active(self):
        if self._game.which_active() == "all":
            print("All boards are active.")
        else:
            x, y = self._game.which_active()
            print(f"Active board: {x+1} row, {y+1} column")

    def generate_row(self, rsq, rpos):
        size = self._size
        print(f"{rsq}.{rpos}", end="")
        rsq -= 1
        rpos -= 1
        for csq in range(size):
            for cpos in range(size):
                print(f"   {self.get_field(rsq, csq, rpos, cpos)}", end="")
            if size-csq-1:
                print("   |", end="")

    def get_field(self, rs, cs, rp, cp):
        val = self._game.get_small_value(rs, cs, rp, cp)
        if not val:
            return FIELDS_EMPTY
        if val == "X":
            return FIELDS_X
        return FIELDS_O

    def generate_endgame(self):
        print("GAME OVER")
        winner = self._game.check_winner()
        if winner == 'tie':
            print("Tie!")
        else:
            print(f"{winner} won the game!")


def main():
    Game()


if __name__ == "__main__":
    main()
