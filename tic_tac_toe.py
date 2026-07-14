import random

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for win in wins:
        if all(board[i] == player for i in win):
            return True
    return False

def is_draw():
    return " " not in board

while True:
    print_board()

    move = int(input("Enter your move (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move! Try again.")
        continue

    board[move] = "X"

    if check_winner("X"):
        print_board()
        print("🎉 You Win!")
        break

    if is_draw():
        print_board()
        print("It's a Draw!")
        break

    ai_moves = [i for i in range(9) if board[i] == " "]
    ai_move = random.choice(ai_moves)
    board[ai_move] = "O"

    print("AI played.")

    if check_winner("O"):
        print_board()
        print("🤖 AI Wins!")
        break

    if is_draw():
        print_board()
        print("It's a Draw!")
        break