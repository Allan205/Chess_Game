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