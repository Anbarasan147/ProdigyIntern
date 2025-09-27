import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("🧩 Sudoku Solver")
        self.root.geometry("500x550")
        self.root.configure(bg="#1e1e2f")

        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()

        # Buttons
        btn_frame = tk.Frame(root, bg="#1e1e2f")
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="✅ Solve", command=self.solve_sudoku, bg="#00adb5", fg="white", font=("Arial", 12, "bold"), width=12).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="🗑️ Clear", command=self.clear_grid, bg="#f05454", fg="white", font=("Arial", 12, "bold"), width=12).grid(row=0, column=1, padx=10)

    def create_grid(self):
        frame = tk.Frame(self.root, bg="#1e1e2f")
        frame.pack(pady=20)

        for i in range(9):
            for j in range(9):
                e = tk.Entry(frame, width=3, font=("Arial", 18), justify="center", bg="#eeeeee")
                e.grid(row=i, column=j, padx=(0 if j % 3 else 3, 3), pady=(0 if i % 3 else 3, 3))
                self.entries[i][j] = e

    def get_grid(self):
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                if val == "":
                    row.append(0)
                else:
                    try:
                        num = int(val)
                        if 1 <= num <= 9:
                            row.append(num)
                        else:
                            messagebox.showerror("Error", "Values must be between 1 and 9")
                            return None
                    except ValueError:
                        messagebox.showerror("Error", "Invalid input! Enter numbers 1-9")
                        return None
            grid.append(row)
        return grid

    def is_valid(self, grid, row, col, num):
        # Row & column check
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False

        # 3x3 box check
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    def display_solution(self, grid):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(grid[i][j]))
                self.entries[i][j].config(fg="green")

    def solve_sudoku(self):
        grid = self.get_grid()
        if grid is None:
            return
        if self.solve(grid):
            self.display_solution(grid)
        else:
            messagebox.showinfo("No Solution", "This Sudoku puzzle cannot be solved!")

    def clear_grid(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].config(fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
