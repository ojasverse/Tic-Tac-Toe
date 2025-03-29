import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        # Initialize the Tkinter window
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        # Initialize game attributes
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.win_combinations = [
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],  # Rows
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],  # Columns
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]  # Diagonals
        ]

        # Initialize buttons attribute
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # Create buttons grid
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.root, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        # Check if the selected cell is empty
        if self.board[row][col] == "":
            # Place the current player's mark on the board
            self.board[row][col] = self.current_player
            # Update the button text
            self.buttons[row][col].config(text=self.current_player)
            # Check for win or draw
            if self.check_win():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif all(self.board[i][j] != "" for i in range(3) for j in range(3)):
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                # Switch to the next player
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        # Check all win combinations
        for combination in self.win_combinations:
            if all(self.board[r][c] == self.current_player for r, c in combination):
                return True
        return False

    def reset_board(self):
        # Reset the board and button texts
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = "X"  # Reset player to "X" when restarting

# Main function to start the game
if __name__ == "__main__":
    game = TicTacToe()
    game.root.mainloop()
