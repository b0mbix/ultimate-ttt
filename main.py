from boards import BigBoard
from bots import RandomBot, SmartBot
from errors import SizeError, RangeError, ActiveError, PlaceError, ModeError
import os
import random


FIELDS_EMPTY = "[ ]"
FIELDS_X = "[X]"
FIELDS_O = "[O]"
BOT = "O"


def clear():
    name = os.name

    if name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class Gameplay:
    """Class responsible for game and interface"""
    def __init__(self):
        self.players = ['X', 'O']
        random.shuffle(self.players)
        clear()
        print("Welcome to Ultimate Tic-Tac-Toe!\n")
        self.get_size()
        self.get_mode()
        while self.game.active:
            if self.players[0] == BOT:
                if self._mode == 1:
                    self.next_move()
                if self._mode in [2, 3]:
                    self._bot.make_move()
            else:
                self.next_move()
        self.generate_board()
        self.generate_endgame()

    def next_move(self):
        self.generate_board()
        self.generate_active()
        print(f"{self.players[0]} move!")
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
            self.game.make_move(rsq, csq, rpos, cpos, self.players[0])
            self.players.reverse()
        except RangeError:
            print("Incorrect move, one or more values are out of range.")
            input("Press Enter to continue...")
        except ActiveError:
            print("This board is not active.")
            input("Press Enter to continue...")
        except PlaceError:
            print("This place is taken or game on this board has ended.")
            input("Press Enter to continue...")

    def get_size(self, next_time=0):
        if not next_time:
            print("Default board size is 3, other sizes are not recommended.")
        try:
            self._size = int(input("Enter board size: "))
            self.game = BigBoard(self._size)
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
            print("2. Player vs random AI")
            print('3. Player vs "smart" AI (not available yet)')
        possible = [1, 2]
        try:
            self._mode = int(input("Enter mode: "))
            if self._mode not in possible:
                raise ModeError
            if self._mode == 2:
                self._bot = RandomBot(self, self._size)
            if self._mode == 3:
                self._bot = SmartBot(self, self._size)
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
        if self.game.which_active() == "all":
            print("All boards are active.")
        else:
            x, y = self.game.which_active()
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
        val = self.game.get_small_value(rs, cs, rp, cp)
        if not val:
            return FIELDS_EMPTY
        if val == "X":
            return FIELDS_X
        return FIELDS_O

    def generate_endgame(self):
        print("GAME OVER")
        winner = self.game.check_winner()
        if winner == 'tie':
            print("Tie!")
        else:
            print(f"{winner} won the game!")


def main():
    Gameplay()


if __name__ == "__main__":
    main()
