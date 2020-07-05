import tkinter as tk
from constants import UiConstants as const
from board import Board
from PIL import Image, ImageTk


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

        self.draw_board()
        self.draw_squares()
        self.draw_pieces()

        self.window.mainloop()

    def draw_board(self):
        self.ui_board = UiBoard()
        self.board_canvas = tk.Canvas(
            self.window,
            bg=self.ui_board.bg_color,
            height=self.ui_board.size,
            width=self.ui_board.size,
            highlightthickness=0
        )
        self.board_canvas.place(
            x=const.windowSize * (1 - const.BOARD_PERCENT_OF_WINDOW) / 2,
            y=const.windowSize * (1 - const.BOARD_PERCENT_OF_WINDOW) / 2
        )

    def draw_squares(self):
        squares = (UiWhiteSquare, UiBlackSquare)

        for i in range(8):
            for j in range(8):
                square = squares[(j + i) % 2]
                x1 = i * square.size
                y1 = j * square.size
                x2 = x1 + square.size
                y2 = y1 + square.size

                self.board_canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=square.bg_color)

    def draw_pieces(self):
        self.board = Board()
        self.images = [[''] * 8 for _ in range(8)]
        canvas = self.board_canvas

        for piece in self.board.pieces:
            rank = piece.get_rank()
            file = piece.get_file()

            image = Image.open('images/' + piece.image).resize(
                (const.squareSize, const.squareSize))

            piece_image = ImageTk.PhotoImage(image)

            self.images[rank][file] = piece_image

            x = (1 + file) * const.squareSize
            y = (8 - rank) * const.squareSize

            canvas.create_image((x, y),
                                anchor=tk.SE,
                                image=piece_image
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
