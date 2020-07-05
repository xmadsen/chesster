import tkinter as tk
from constants import UiConstants as const
from board import Board


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


class UserInterface():

    def __init__(self):
        self.draw_window()

    def draw_window(self):
        self.window = tk.Tk()
        self.window.title("Chesster")
        self.window.resizable(0, 0)
        self.window.configure(bg='grey29')
        self.window.geometry("{}x{}".format(
            const.windowSize, const.windowSize))
        label = tk.Label(
            self.window, text="This is Chesster, the Chess app")

        self.add_board()
        self.add_squares()

        self.window.mainloop()

    def add_board(self):
        self.ui_board = UiBoard()
        board_frame = tk.Frame(
            self.window,
            bg=self.ui_board.bg_color,
            height=self.ui_board.size,
            width=self.ui_board.size
        )
        board_frame.place(
            x=const.windowSize * (1 - const.BOARD_PERCENT_OF_WINDOW) / 2,
            y=const.windowSize * (1 - const.BOARD_PERCENT_OF_WINDOW) / 2
        )

    def add_squares(self):
        squares = (UiBlackSquare, UiWhiteSquare)

        board_frame = self.window.winfo_children()[1]

        for i in range(8):
            for j in range(8):
                square = squares[(j + i) % 2]
                new_square = tk.Frame(
                    board_frame,
                    bg=square.bg_color,
                    height=square.size,
                    width=square.size)
                self.ui_board.squares[i][7 - j] = new_square

                new_square.place(
                    x=board_frame.winfo_x() + square.size * i,
                    y=board_frame.winfo_y() + square.size * (7 - j)
                )


class UiBoard():
    size = const.boardSize
    bg_color = _from_rgb((49, 46, 43))
    bd = 5

    squares = [[""] * 8 for _ in range(8)]


class UiSquare():
    size = const.squareSize


class UiBlackSquare(UiSquare):
    bg_color = _from_rgb((122, 146, 92))


class UiWhiteSquare(UiSquare):
    bg_color = _from_rgb((220, 220, 197))
