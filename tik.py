# define a function to print the tic-tac-toe board
def print_board(board):
  # loop through each row
  for i in range(3):
    # print the row
    print("|".join(board[i]))

# define the initial tic-tac-toe board
board = [
  [" ", " ", " "],
  [" ", " ", " "],
  [" ", " ", " "]
]

# print the initial board
print_board(board)

# prompt the user to make their first move
move = input("Enter your move (1-9): ")

# update the board with the user's move
# (assuming the move is in the top left corner)
board[0][0] = "X"

# print the updated board
print_board(board)




