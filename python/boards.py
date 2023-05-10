from pprint import pprint
from random import randint


def square_board(n, open_square = " "):
    return [[open_square for i in range(n)] for j in range(n)]


def rect_board(width, height, open_square = " "):
    return [[open_square for i in range(width)] for j in range(height)]


def update_squares(board, func):
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            board[i][j] = func(col, i, j)
    return board


def checker_squares(board, type1, type2):
    return update_squares(board, lambda a, b, c: type1 if (b + c) % 2 == 0 else type2)


def clear_board(board, open_square=" "):
    return update_squares(board, lambda a, b, c: open_square)


def change_one_square(board, i, j, change):
    board[i][j] = change
    return board


def change_squares(board, squares, change):
    for square in squares:
        change_one_square(board, square[0], square[1], change)
    return board


def flip_board_y(board):
    for row in board:
        row.reverse()
    return board


def flip_board_x(board):
    flip_board_y(board).reverse()
    return board


def get_row(board, row):
    return board[row]


def get_column(board, col):
    return [row[col] for row in board]


def get_square(board, i, j):
    return board[i][j]


def clear_square(board, i, j, open_square=" "):
    return change_one_square(board, i, j, open_square)


def clear_row(board, row, open_square=""):
    board[row] = [open_square for col in board[row]]
    return board


def clear_col(board, col, open_square=" "):
    for row in board:
        row[col] = open_square
    return board


def add_large_item_to_row(board, row, col, item):
    if col + len(item) >= len(board[row]):
        return "It doesn't fit!!!"
    for piece in item:
        board[row][col] = piece
        col += 1
    return board


def add_large_item_to_col(board, row, col, item):
    if row + len(item) >= len(board):
        return "It doesn't fit!!!"
    for piece in item:
        board[row][col] = piece
        row += 1
    return board


def add_item_diag_rising_right(board, row, col, item):
    if row - len(item) < 0 or col + len(item) >= len(board[0]):
        return "It doesn't fit!!!"
    for piece in item:
        board[row][col] = piece
        row -= 1
        col += 1
    return board


def add_item_diag_falling_right(board, row, col, item):
    if row + len(item) >= len(board) or col + len(item) >= len(board[0]):
        return "It doesn't fit!!!"
    for piece in item:
        board[row][col] = piece
        row += 1
        col += 1
    return board


def add_item_diag_rising_left(board, row, col, item):
    if row - len(item) < 0 or col - len(item) < 0:
        return "It doesn't fit!!!"
    for piece in item:
        board[row][col] = piece
        row -= 1
        col -= 1
    return board


def add_item_diag_falling_left(board, row, col, item):
    if row + len(item) >= len(board) or col - len(item) < 0:
        return "It doesn't fit!!!"
    for piece in item:
        board[row][col] = piece
        row += 1
        col -= 1
    return board


def add_n_items_randomly(board, quantity, item):
    w, h, cache = len(board[0]), len(board), {}
    while quantity:
        point = [randint(0, h -1), randint(0, w - 1)]
        if not cache.get(str(point)):
            cache[str(point)] = point
            quantity -= 1
    for point in cache:
        board[cache[point][0]][cache[point][1]] = item
    return board


def drop_into_col(board, col, item, open=" "):
    for i in range(len(board) -1, -1, -1):
        if board[i][col] == open:
            board[i][col] = item
            break
    return board


# TESTS -------------------------------------------------------------

test = square_board(7, "hi")
print("\n")

pprint(test)
print("\n")

test = checker_squares(test, "-", 'O')
print("\n")
pprint(test)

test = change_one_square(test, 0, 0, "hi")
print("\n")
pprint(test)

test = flip_board_x(test)
print("\n")
pprint(test)

test = add_item_diag_rising_left(test, 6, 5, "MMMM")
print("\n")
pprint(test)

# test = clear_board(test)
# print("\n")
# pprint(test)








