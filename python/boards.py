from pprint import pprint
from random import randint

class GameBoard:
    def __init__(self, width, **board_specs):
        self.width = width
        self.height = board_specs["height"] if board_specs.get("height") else width
        self.open = board_specs["open"] if board_specs.get("open") else " "
        self.board = self.create_board()

    def create_board(self):
        return [[self.open for i in range(self.width)] for j in range(self.height)]

    def update_squares(self, func):
        for i, row in enumerate(self.board):
            for j, square in enumerate(row):
                self.board[i][j] = func(square, i, j)

    def checker_squares(self, type1, type2):
        self.update_squares(lambda a, b, c: type1 if (b + c) % 2 == 0 else type2)

    def get_square(self, i, j):
        return self.board[i][j]

    def get_row(self, row):
        return self.board[row]

    def get_column(self, col):
        return [row[col] for row in self.board]

    def change_one_square(self, i, j, change):
        self.board[i][j] = change

    def change_squares(self, squares, change):
        for square in squares:
            self.change_one_square(square[0], square[1], change)

    def flip_board_y(self):
        for row in self.board:
            row.reverse()

    def flip_board_x(self):
        self.board.reverse()

    def rotate_board_180(self):
        self.flip_board_y()
        self.flip_board_x()

    def clear_board(self):
        self.update_squares(lambda a, b, c: self.open)

    def clear_square(self, i, j):
        self.change_one_square(i, j)

    def clear_row(self, row):
        self.board[row] = [self.open for col in self.board[row]]

    def clear_col(self, col):
        for row in self.board:
            row[col] = self.open

    def add_large_item_to_row(self, row, col, item):
        if col + len(item) > len(self.board[row]):
            return "It doesn't fit!!!"
        for piece in item:
            self.board[row][col] = piece
            col += 1

    def add_large_item_to_col(self, row, col, item):
        if row + len(item) > len(self.board):
            return "It doesn't fit!!!"
        for piece in item:
            self.board[row][col] = piece
            row += 1

    def add_item_diag_rising_left(self, row, col, item):
        if row - len(item) < -1 or col - len(item) < -1:
            return "It doesn't fit!!!"
        for piece in item:
            self.board[row][col] = piece
            row -= 1
            col -= 1

    def add_item_diag_rising_right(self, row, col, item):
        if row - len(item) < -1 or col + len(item) > len(self.board[0]):
            return "It doesn't fit!!!"
        for piece in item:
            self.board[row][col] = piece
            row -= 1
            col += 1

    def add_item_diag_falling_left(self, row, col, item):
        if row + len(item) > len(self.board) or col - len(item) < -1:
            return "It doesn't fit!!!"
        for piece in item:
            self.board[row][col] = piece
            row += 1
            col -= 1

    def add_item_diag_falling_right(self, row, col, item):
        if row + len(item) > len(self.board) or col + len(item) > len(self.board[0]):
            return "It doesn't fit!!!"
        for piece in item:
            self.board[row][col] = piece
            row += 1
            col += 1

    def add_n_items_randomly(self, quantity, item):
        w, h, cache = len(self.board[0]), len(self.board), {}
        while quantity:
            point = [randint(0, h -1), randint(0, w - 1)]
            if not cache.get(str(point)):
                cache[str(point)] = point
                quantity -= 1
        for point in cache:
            self.board[cache[point][0]][cache[point][1]] = item

    def drop_into_col(self, col, item):
        for i in range(self.height -1, -1, -1):
            if self.board[i][col] == self.open:
                self.board[i][col] = item
                break
































