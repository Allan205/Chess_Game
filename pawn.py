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

    #One Square Forward
    if (
        row_change == direction and
        column_change == 0 and
        board[row][column] == ""
        ):
        return True

    #Two Squares Forward
    middle_row = start_row + direction
    if (
        start_row == starting_row and
        row_change == (direction * 2 )and
        column_change == 0 and
        board[middle_row][start_column] == "" and
        board[row][column] == ""
    ):
        return True

    #Capture
    if (
        row_change == direction and
        abs(column_change) == 1
    ):
        captured_piece = board[row][column]
        if selected_piece == "♙" and captured_piece in ["♟", "♜", "♞", "♝", "♛", "♚"]:
            return True

        if selected_piece == "♟" and captured_piece in ["♙", "♖", "♘", "♗", "♕", "♔"]:
            return True

    return False