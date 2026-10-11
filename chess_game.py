import turtle

screen = turtle.Screen()
board_t = turtle.Turtle()
board_t.hideturtle()
pieces_t = turtle.Turtle()
pieces_t.hideturtle()
message_t = turtle.Turtle()
message_t.hideturtle()
board_t.speed(0)
pieces_t.speed(0)
message_t.speed(0)
start_x = -250
start_y = 200
size = 60
game_over = False

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

def find_king(board, color):
    if color == "white":
        king = "♔"
    else:
        king = "♚"

    for row in range(8):
        for column in range(8):
            if board[row][column] ==  king:
                return (row, column)

def king_under_attack(board, king_row, king_column, attacking_color):
    for row in range(8):
        for column in range(8):
            piece = board[row][column]

            if piece == "":
                continue
            if piece_color(piece) != attacking_color:
                continue

            selected_piece = piece
            selected_square = (row, column)

            if piece in ["♟", "♙"]:
                if valid_pawn_move(board, selected_piece, selected_square, king_row, king_column):
                    return True
            elif piece in ["♜", "♖"]:
                if valid_rook_move(board, selected_piece, selected_square, king_row, king_column):
                    return True
            elif piece in ["♞", "♘"]:
                if valid_knight_move(board, selected_piece, selected_square, king_row, king_column):
                    return True
            elif piece in ["♝", "♗"]:
                if valid_bishop_move(board, selected_piece, selected_square, king_row, king_column):
                    return True
            elif piece in ["♛", "♕"]:
                if valid_queen_move(board, selected_piece, selected_square, king_row, king_column):
                    return True
            elif piece in ["♚", "♔"]:
                if valid_king_move(board, selected_piece, selected_square, king_row, king_column):
                    return True

    return False

def king_is_in_check(board, color):
    king_row, king_column = find_king(board, color)

    if color == "white":
        attacking_color = "black"
    else:
        attacking_color = "white"

    return king_under_attack(board, king_row, king_column, attacking_color)

def move_leaves_king_in_check(board, selected_square, row, column, turn):
    original_row, original_column = selected_square
    new_row = row
    new_column = column

    piece = board[original_row][original_column]
    captured_piece = board[new_row][new_column]
    board[new_row][new_column] = piece
    board[original_row][original_column] = ""

    check_status = king_is_in_check(board, turn)

    board[new_row][new_column] = captured_piece
    board[original_row][original_column] = piece

    return check_status

def king_can_escape(board, turn):
    king_row, king_column = find_king(board, turn)
    escape_positions = [(king_row, king_column + 1), (king_row, king_column -1), (king_row + 1, king_column), (king_row - 1, king_column),
                        (king_row + 1, king_column + 1), (king_row + 1, king_column - 1), (king_row - 1, king_column + 1), (king_row - 1, king_column - 1)]
    
    for position in escape_positions:
        selected_piece = board[king_row][king_column]
        selected_square = (king_row, king_column)
        row, column = position

        if row < 0 or row > 7 or column < 0 or column > 7:
            continue
        if valid_king_move(board, selected_piece, selected_square, row, column):
            if not move_leaves_king_in_check(board, selected_square, row, column, turn):
                return True

    return False

def find_attacking_piece(board, king_row, king_column, turn):
    for row in range(8):
        for column in range(8):
            attacking_piece = board[row][column]
            selected_square = (row, column)

            if attacking_piece == "":
                continue
            if piece_color(attacking_piece) == turn:
                continue

            if move_is_valid(board, attacking_piece, selected_square, king_row, king_column):
                return row, column

    return None

def capture_attacking_piece(board, king_row, king_column, turn):
    if find_attacking_piece(board, king_row, king_column, turn) == None:
        return False
    attacking_row, attacking_column = find_attacking_piece(board, king_row, king_column, turn)

    for row in range(8):
        for column in range(8):
            piece = board[row][column]
            selected_square = (row, column)
            if piece == "":
                continue
            if piece_color(piece) != turn:
                continue
            if move_is_valid(board, piece, selected_square, attacking_row, attacking_column):
                if not move_leaves_king_in_check(board, selected_square, attacking_row, attacking_column, turn):
                    return True

    return False

def block_attacking_piece(board, king_row, king_column, turn):
    if find_attacking_piece(board, king_row, king_column, turn) is None:
        return False
    attacking_row, attacking_column = find_attacking_piece(board, king_row, king_column, turn)
    attacking_piece = board[attacking_row][attacking_column]
    if attacking_piece not in ["♜", "♖", "♝", "♗", "♛", "♕"]:
        return False

    row_step = 0
    column_step = 0
    if attacking_row < king_row:
        row_step = 1
    elif attacking_row > king_row:
        row_step = -1
    if attacking_column < king_column:
        column_step = 1
    elif attacking_column > king_column:
        column_step = -1

    row = attacking_row + row_step
    column = attacking_column + column_step
    blocking_positions = []

    while (row, column) != (king_row, king_column):
        blocking_positions.append((row, column))
        row += row_step
        column += column_step

    for row in range(8):
        for column in range(8):
            piece = board[row][column]
            if piece == "":
                continue
            if piece_color(piece) != turn:
                continue

            selected_square = (row, column)
            for block_row, block_column in blocking_positions:
                if move_is_valid(board, piece, selected_square, block_row, block_column):
                    if not move_leaves_king_in_check(board, selected_square, block_row, block_column, turn):
                        return True

    return False

def king_is_ckeckmate(board, king_row, king_column, turn):
    if not king_is_in_check(board, turn):
        return False
    
    if(
        not king_can_escape(board, turn) and
        not capture_attacking_piece(board, king_row, king_column, turn) and
        not block_attacking_piece(board, king_row, king_column, turn)
    ):
        return True
    else:
        return False

selected_square = None
selected_piece = None
turn = "white"

def move_is_valid(board, selected_piece, selected_square, row, column):
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
        
    return valid_move

def move_piece(board, selected_piece, selected_square, row, column, turn):
    start_row, start_column = selected_square

    valid_move = move_is_valid(board, selected_piece, selected_square, row, column)
    if valid_move == True:
        if move_leaves_king_in_check(board, selected_square, row, column, turn):
            return False
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
    global game_over
    if game_over:
        return
    
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
        valid_move = move_piece(board, selected_piece, selected_square, row, column, turn)
        if valid_move == True:
            if turn == "white":
                turn = "black"
            else:
                turn = "white"

        king_row, king_column = find_king(board, turn)
        if king_is_ckeckmate(board, king_row, king_column, turn):
            game_over = True
            message_t.penup()
            message_t.goto(-250, -350)
            message_t.write(f"Checkmate\n'{turn}' loses", align="left", font=("Times New Roman", 14, "bold"))
                
        selected_piece = None
        selected_square = None
        redraw()

draw_board()
draw_pieces()
screen.onclick(mouse_click)

turtle.done()