from boards import Board, BigBoard, SmallBoard
from boards import SizeError
import os


FIELDS_EMPTY = "[ ]"
FIELDS_X = "[X]"
FIELDS_O = "[O]"


class ModeError(Exception):
    pass


def clear():
    os.system("clear")


class Game:
    def __init__(self):
        clear()
        print("Welcome to Ultimate Tic-Tac-Toe!\n")
        self.get_size()
        self.get_mode()
        self.generate_ui()

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

    def generate_ui(self):
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

    def generate_row(self, rsq, rpos):
        size = self._size
        print(f"{rsq}.{rpos}", end="")
        for i in range(size):
            for j in range(size):
                print(f"   {FIELDS_EMPTY}", end="")
            if size-i-1:
                print("   |", end="")


def main():
    Game()


if __name__ == "__main__":
    main()
