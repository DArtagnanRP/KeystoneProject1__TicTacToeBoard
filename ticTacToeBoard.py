"""def initial_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row1 = [board[0], board[1], board[2]]
    row2 = [board[3], board[4], board[5]]
    row3 = [board[6], board[7], board[8]]


def display(board, row1, row2, row3):
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row1 = [board[0], board[1], board[2]]
    row2 = [board[3], board[4], board[5]]
    row3 = [board[6], board[7], board[8]]
    print(row1)
    print(row2)
    print(row3)
    return board


# "initial_board"()
display(board=None, row1=None, row2=None, row3=None)"""
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
row1 = [board[0], board[1], board[2]]
row2 = [board[3], board[4], board[5]]
row3 = [board[6], board[7], board[8]]


def board_reassign(a=None):
    """board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row1 = [board[0], board[1], board[2]]
    row2 = [board[3], board[4], board[5]]
    row3 = [board[6], board[7], board[8]]"""
    if a is None:
        a = board
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return a


def row_reassign(a=board, x=row1, y=row2, z=row3):
    x = [board[0], board[1], board[2]]
    y = [board[3], board[4], board[5]]
    z = [board[6], board[7], board[8]]
    return (x,y,z)


def display(a=board, x=row1, y=row2, z=row3):
    print(x)
    print(y)
    print(z)
    return a

display()
board[0]="hello"

Hello = row_reassign(board, row1, row2, row3)
print(Hello[1])
row1 = Hello[0]
print(row1)

print(board)

board_reassign(board)

display(a=board, x=row1, y=row2, z=row3)