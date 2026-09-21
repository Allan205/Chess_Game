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