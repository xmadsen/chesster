class UiConstants():
    windowSize = 600

    BOARD_PERCENT_OF_WINDOW = 0.9
    boardSize = int(windowSize * BOARD_PERCENT_OF_WINDOW)

    squareSize = int(boardSize / 8)


class PieceConstants():
    WHITE_COLOR = 17
    BLACK_COLOR = 31
    SELECTED_BG_COLOR = 42
    UNSELECTED_BG_COLOR = 40


class PlayerConstants():
    WHITE_PLAYER = "White"
    BLACK_PLAYER = "Black"
