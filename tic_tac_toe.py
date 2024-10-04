import tkinter as tk
from tkinter import messagebox


# Function to check if there's a winner.
def check_winner():
    for i in range(3):
        # Check rows and columns.
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    # Check diagonals.
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None


# Function for button clicks.
def button_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "" and not game_over:
        buttons[row][col]["text"] = current_player
        board[row][col] = current_player
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif all(all(cell != "" for cell in row) for row in board):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"


# Function to reset the game.
def reset_game():
    global board, current_player, game_over
    current_player = "X"
    game_over = False
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
# Initializing tkinter window.
root = tk.Tk()
root.title("Tic-Tac-Toe")
# Global variables.
current_player = "X"
game_over = False
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
# Creating buttons for the board.
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", width=10, height=3, font=("Arial", 24),
                                      command=lambda row=row, col=col: button_click(row, col))
        buttons[row][col].grid(row=row, column=col)
# Running the window.
reset_game()
root.mainloop()
