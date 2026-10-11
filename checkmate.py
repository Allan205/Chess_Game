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