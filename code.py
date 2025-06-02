def print_board(board):
    print("Current board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column from 1 to 3, separated by space): ")
            row, col = map(int, move.strip().split())
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Invalid input. Row and column must be between 1 and 3.")
                continue
            if board[row-1][col-1] != " ":
                print("That position is already taken. Try again.")
                continue
            return row-1, col-1
        except ValueError:
            print("Invalid input format. Please enter row and column as two numbers separated by space.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_move(current_player, board)
        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    play_game()

