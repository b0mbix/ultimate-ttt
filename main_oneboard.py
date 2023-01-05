from PySide2.QtWidgets import QApplication, QMainWindow
from ui_oneboard_responsible import Ui_MainWindow
from boards import Board
import sys


class oneBoardWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.game = Board()
        self.players = ["X", "O"]
        self.ui.squares.buttonClicked.connect(self._squareClicked)
        self._set_move_text()

    def _squareClicked(self, button):
        x = int(button.objectName()[7])
        y = int(button.objectName()[8])
        to_reverse = 0 if self.game.fields[x][y] else 1
        self.game.make_move(x, y, self.players[0])
        if self.game.fields[x][y]:
            button.setText(self.game.fields[x][y])
        if to_reverse:
            self.players.reverse()
        self._set_move_text()

    def _set_move_text(self):
        winner = self.game.check_winner()
        if winner:
            self.ui.move_label.setText(f"{winner} won the game!")
            if winner == "tie":
                self.ui.move_label.setText("Tie!")
        else:
            self.ui.move_label.setText(f"Move: {self.players[0]}")


def guiMain(args):
    app = QApplication(args)
    window = oneBoardWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
