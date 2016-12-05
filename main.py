
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
        f = self.board[start.i][start.j]
        self.board[destination.i][destination.j] = f
        self.board[start.i][start.j] = EMPTY_SQUARE


class BoardLocation(object):
    def __init__(self, i, j):
        self.i = i
        self.j = j


class View(object):
    def display(self, board):
        print("%s: %s" % (" ", column_reference))
        print("-" * 43)
        for i, row in enumerate(board):
            row_marker = 8 - i
            print("%s: %s" % (row_marker, row))


class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            self.view.display(self.model.board)
            move = raw_input("move (exemple e2-e5 or quit) ")
            move = move.lower()
            if move == "quit":
                break
            start, destination = self.basic_movement(move)
            self.model.move(start, destination)

    def basic_movement(self, move):
        s, d = move.split("-")

        i = 8 - int(s[-1])
        j = column_reference.index(s[0])
        start = BoardLocation(i, j)

        i = 8 - int(d[-1])
        j = column_reference.index(d[0])
        destination = BoardLocation(i, j)

        return start, destination


if __name__ == "__main__":
    C = Controller()
    C.run()
