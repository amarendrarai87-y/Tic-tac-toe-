import numpy as np   


board = ["1","2","3",
         "4","5","6",
         "7","8","9"]


winning_moves = (
    (0, 1, 2),   
    (3, 4, 5),   
    (6, 7, 8),   
    (0, 3, 6),   
    (1, 4, 7),  
    (2, 5, 8),   
    (0, 4, 8),   
    (2, 4, 6)    
)


def display_board():
    print(np.array(board).reshape(3, 3))
    print()


def check_winner(player):
    for a, b, c in winning_moves:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


print("=== TIC TAC TOE ===")
print("Player 1 = X")
print("Player 2 = O")
print()

display_board()

current_player = "X"

while True:
    choice = input(f"Player {current_player}, choose a position (1-9): ")

    
    if choice not in board:
        print("Invalid move! Try again.\n")
        continue

   
    index = board.index(choice)
    board[index] = current_player

    display_board()

    
    if check_winner(current_player):
        print(f"🎉 Player {current_player} wins!")
        break

    
    if all(x in ("X", "O") for x in board):
        print("It's a draw!")
        break

    
    current_player = "O" if current_player == "X" else "X"
