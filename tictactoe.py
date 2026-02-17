import random

# Create board
board = [" " for x in range(9)]

# Print board
def print_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# Check winner
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Check draw
def check_draw():
    return " " not in board

# Player move
def player_move():
    while True:
        move = int(input("Enter position (1-9): ")) - 1
        if board[move] == " ":
            board[move] = "X"
            break
        else:
            print("Position already taken! Try again.")

# Computer move
def computer_move():
    print("Computer's turn...")
    available_positions = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_positions)
    board[move] = "O"

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, Computer is O")

    while True:
        print_board()
        player_move()

        if check_winner("X"):
            print_board()
            print("Congratulations! You win!")
            break

        if check_draw():
            print_board()
            print("It's a draw!")
            break

        computer_move()

        if check_winner("O"):
            print_board()
            print("Computer wins!")
            break

        if check_draw():
            print_board()
            print("It's a draw!")
            break

play_game()
