
column_reference = "a b c d e f g h".split(" ")
EMPTY_SQUARE = " "


class Model(object):
    def __init__(self):

        self.board = []
        white_pieces = "R N B Q K B N R"
        white_pawns = "P P P P P P P P"
        black_pieces = "r n b q k b n r"
        black_pawns = "p p p p p p p p"
        self.board.append(black_pieces.split(" "))
        self.board.append(black_pawns.split(" "))
        for i in range(4):
            self.board.append([EMPTY_SQUARE] * 8)
        self.board.append(white_pawns.split(" "))
        self.board.append(white_pieces.split(" "))

    def move(self, start, destination):
        for c in [start, destination]:
            f = self.board[start.i][start.j]
            self.board[destination.i][destination.j] = f

