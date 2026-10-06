import turtle

screen = turtle.Screen()
board_t = turtle.Turtle()
pieces_t = turtle.Turtle()
board_t.speed(0)
pieces_t.speed(0)
start_x = -250
start_y = 200
size = 60

board = [
    ["♜","♞","♝","♛","♚","♝","♞","♜"],
    ["♟","♟","♟","♟","♟","♟","♟","♟"],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["♙","♙","♙","♙","♙","♙","♙","♙"],
    ["♖","♘","♗","♕","♔","♗","♘","♖"]
]   

def draw_board():
    for row in range(8):
        for column in range(8):
            x_position = start_x + (column * size)
            y_position = start_y - (row * size)
            board_t.penup()
            board_t.goto(x_position, y_position)
            board_t.pendown()

            if (row + column) % 2 != 0:
                color = "brown"
            if (row + column) % 2 == 0:
                color = "white"

            board_t.fillcolor(color)
            board_t.begin_fill()
            for i in range(4):
                board_t.forward(size)
                board_t.right(90)
            board_t.end_fill()

def draw_pieces():
    for row in range(8):
        for column in range(8):
            symbol = board[row][column]
            center_x = start_x + (column * size) + (size / 2)
            center_y = start_y - (row * size) - (size / 2)
            if symbol != "":
                pieces_t.penup()
                pieces_t.goto(center_x, (center_y - 25))
                pieces_t.pendown()
                pieces_t.write(symbol, align="center", font=("Arial", 32, "normal"))

def valid_pawn_move(board, selected_piece, selected_square, row, column):
    start_row, start_column = selected_square
    row_change = row - start_row
    column_change = column - start_column

    if selected_piece == "♟":
        starting_row = 1
        direction = 1
    elif selected_piece == "♙":
        starting_row = 6
        direction = -1

    if (
        row_change == direction and
        column_change == 0 and
        board[row][column] == ""
        ):
        return True

    middle_row = start_row + direction
    if (
        start_row == starting_row and
        row_change == (direction * 2 )and
        column_change == 0 and
        board[middle_row][start_column] == "" and
        board[row][column] == ""
    ):
        return True

    if (
        row_change == direction and
        abs(column_change) == 1
    ):
        destination = board[row][column]
        if selected_piece == "♙" and destination in ["♟", "♜", "♞", "♝", "♛", "♚"]:
            return True

        if selected_piece == "♟" and destination in ["♙", "♖", "♘", "♗", "♕", "♔"]:
            return True

    return False

def valid_knight_move(board, selected_piece, selected_square, row, column):
    start_row, start_column = selected_square
    row_change = row - start_row
    column_change = column - start_column

    white_pieces = ["♙", "♖", "♘", "♗", "♕", "♔"]
    black_pieces = ["♟", "♜", "♞", "♝", "♛", "♚"]

    if not (
        abs(row_change) == 2 and abs(column_change) == 1 or
        abs(row_change) == 1 and abs(column_change) == 2
    ):
        return False

    destination = board[row][column]

    if selected_piece in white_pieces:
        if destination in white_pieces:
            return False
    elif selected_piece in black_pieces:
        if destination in black_pieces:
            return False

    return True

def valid_rook_move(board, selected_piece, selected_square, row, column):
    start_row, start_column = selected_square
    row_change = row - start_row
    column_change = column - start_column

    white_pieces = ["♙", "♖", "♘", "♗", "♕", "♔"]
    black_pieces = ["♟", "♜", "♞", "♝", "♛", "♚"]

    if row_change != 0 and column_change != 0:
        return False

    if column_change == 0:
        if row_change > 0:
            step = 1
        elif row_change < 0:
            step = -1
        for current_row in range(start_row + step, row, step):
            if board[current_row][start_column] != "":
                return False

    if row_change == 0:
        if column_change > 0:
            step = 1
        elif column_change < 0:
            step = -1
        for current_column in range(start_column + step, column, step):
            if board[start_row][current_column] != "":
                return False

    destination = board[row][column]
    if selected_piece in white_pieces:
        if destination in white_pieces:
            return False
    elif selected_piece in black_pieces:
        if destination in black_pieces:
            return False

    return True

def valid_bishop_move(board, selected_piece, selected_square, row, column):
    start_row, start_column = selected_square
    row_change = row - start_row
    column_change = column - start_column
    
    white_pieces = ["♙", "♖", "♘", "♗", "♕", "♔"]
    black_pieces = ["♟", "♜", "♞", "♝", "♛", "♚"]

    if abs(row_change) != abs(column_change):
        return False

    if row_change > 0:
        row_step = 1
    elif row_change < 0:
        row_step = -1
    if column_change > 0:
        column_step = 1
    elif column_change < 0:
        column_step = -1

    current_row = start_row + row_step
    current_column = start_column + column_step

    for i in range(abs(row_change) - 1):
        if board[current_row][current_column] != "":
            return False
        else:
            current_row += row_step
            current_column += column_step

    destination = board[row][column]
    if selected_piece in white_pieces:
        if destination in white_pieces:
            return False
    elif selected_piece in black_pieces:
        if destination in black_pieces:
            return False

    return True

def valid_queen_move(board, selected_piece, selected_square, row, column):
    if valid_rook_move(board, selected_piece, selected_square, row, column) == True:
        return True
    if valid_bishop_move(board, selected_piece, selected_square, row, column) == True:
        return True

    return False

def valid_king_move(board, selected_piece, selected_square, row, column):
    start_row, start_column = selected_square
    row_change = row - start_row
    column_change = column - start_column
    
    white_pieces = ["♙", "♖", "♘", "♗", "♕", "♔"]
    black_pieces = ["♟", "♜", "♞", "♝", "♛", "♚"]

    if row_change == 0 and column_change == 0:
        return False
    if abs(row_change) > 1 or abs(column_change) > 1:
        return False

    destination = board[row][column]
    if selected_piece in white_pieces:
        if destination in white_pieces:
            return False
    elif selected_piece in black_pieces:
        if destination in black_pieces:
            return False

    return True

selected_square = None
selected_piece = None
turn = "white"

def move_piece(board, selected_piece, selected_square, row, column):
    start_row, start_column = selected_square

    if selected_piece == "♟" or selected_piece == "♙":
        valid_move = valid_pawn_move(board, selected_piece, selected_square, row, column)
    elif selected_piece == "♞" or selected_piece == "♘":
        valid_move = valid_knight_move(board, selected_piece, selected_square, row, column)
    elif selected_piece == "♜" or selected_piece == "♖":
        valid_move = valid_rook_move(board, selected_piece, selected_square, row, column)
    elif selected_piece == "♝" or selected_piece == "♗":
        valid_move = valid_bishop_move(board, selected_piece, selected_square, row, column)
    elif selected_piece == "♛" or selected_piece == "♕":
        valid_move = valid_queen_move(board, selected_piece, selected_square, row, column)
    elif selected_piece == "♚" or selected_piece == "♔":
        valid_move = valid_king_move(board, selected_piece, selected_square, row, column)

    if valid_move == True:
        board[row][column] = selected_piece
        board[start_row][start_column] = ""
        return True
    
    return False

def redraw():
    pieces_t.clear()
    draw_pieces()

def define_boundaries(start_x, start_y, size, x, y):
    left = start_x
    right = start_x + (size * 8)
    top = start_y
    bottom = start_y - (size * 8)

    if (
        left <= x <= right and
        bottom <= y <= top
    ):
        return True


def coordinates_to_square(x, y):
    row = int((start_y - y) / size)
    column = int((x - start_x) / size)

    return row, column

def piece_color(piece):
    white_pieces = ["♙", "♖", "♘", "♗", "♕", "♔"]
    black_pieces = ["♟", "♜", "♞", "♝", "♛", "♚"]

    if piece in white_pieces:
        return "white"
    elif piece in black_pieces:
        return "black"

def mouse_click(x, y):
    inside_square = define_boundaries(start_x, start_y, size, x, y)
    if inside_square != True:
        return

    row, column = coordinates_to_square(x, y)
    global selected_piece, selected_square, turn

    if selected_square == None:
        if board[row][column] == "":
            return
        piece = board[row][column]
        if piece_color(piece) != turn:
            return
        selected_square = (row, column)
        selected_piece = board[row][column]
    else:
        valid_move = move_piece(board, selected_piece, selected_square, row, column)
        if valid_move == True:
            if turn == "white":
                turn = "black"
            else:
                turn = "white"
                
        selected_piece = None
        selected_square = None
        redraw()

draw_board()
draw_pieces()
screen.onclick(mouse_click)

turtle.done()