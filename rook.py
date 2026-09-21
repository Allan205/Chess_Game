def valid_rook_move(board, selected_piece, selected_square, row, column):
    start_row, start_column = selected_square
    row_change = row - start_row
    column_change = column - start_column

    white_pieces = ["♙", "♖", "♘", "♗", "♕", "♔"]
    black_pieces = ["♟", "♜", "♞", "♝", "♛", "♚"]

    if row_change != 0 and column_change != 0:
        return False

    #Vertical Movement
    if column_change == 0:
        if row_change > 0:
            step = 1
        elif row_change < 0:
            step = -1
        for current_row in range(start_row + step, row, step):
            if board[current_row][start_column] != "":
                return False

    #Horizontal Movement
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