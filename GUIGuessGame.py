import tkinter as tk
import random
import time

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Guessing Game 🎨")
        self.root.geometry("450x500")
        self.root.configure(bg="#222831")  # Dark background

        self.number = None
        self.attempts = 0
        self.start_time = None

        # Title
        self.title_label = tk.Label(
            root,
            text="🎮 Welcome to the Guessing Game! 🎮",
            font=("Comic Sans MS", 16, "bold"),
            fg="#ffd369",
            bg="#222831"
        )
        self.title_label.pack(pady=15)

        # Difficulty selection
        self.difficulty_label = tk.Label(
            root,
            text="Choose Difficulty:",
            font=("Arial", 12, "bold"),
            fg="#eeeeee",
            bg="#222831"
        )
        self.difficulty_label.pack()

        self.difficulty_var = tk.StringVar(value="easy")
        difficulties = ["easy", "medium", "hard"]
        colors = ["#32e0c4", "#f96d00", "#f05454"]

        for diff, color in zip(difficulties, colors):
            tk.Radiobutton(
                root,
                text=diff.capitalize(),
                variable=self.difficulty_var,
                value=diff,
                fg=color,
                bg="#222831",
                font=("Arial", 11, "bold"),
                selectcolor="#393e46",
                activebackground="#222831"
            ).pack(pady=2)

        # Start button
        self.start_button = tk.Button(
            root,
            text="🚀 Start Game",
            command=self.start_game,
            bg="#00adb5",
            fg="white",
            font=("Arial", 13, "bold"),
            relief="raised",
            bd=3,
            width=15
        )
        self.start_button.pack(pady=15)

        # Guess input & button
        self.guess_entry = tk.Entry(root, font=("Arial", 13), justify="center", bg="#eeeeee")
        self.guess_button = tk.Button(
            root,
            text="🎯 Guess",
            command=self.make_guess,
            bg="#f96d00",
            fg="white",
            font=("Arial", 13, "bold"),
            relief="raised",
            bd=3,
            width=10
        )

        # Result label
        self.result_label = tk.Label(
            root,
            text="",
            font=("Arial", 12, "bold"),
            fg="#eeeeee",
            bg="#000000"
        )
        self.result_label.pack(pady=15)

    def start_game(self):
        difficulty = self.difficulty_var.get()
        if difficulty == "easy":
            self.number = random.randint(1, 20)
            self.max_attempts = 10
        elif difficulty == "medium":
            self.number = random.randint(1, 50)
            self.max_attempts = 8
        else:
            self.number = random.randint(1, 100)
            self.max_attempts = 7

        self.attempts = 0
        self.start_time = time.time()
        self.result_label.config(text=f"Game started! 🎲 You have {self.max_attempts} attempts.")

        self.guess_entry.pack(pady=5)
        self.guess_button.pack(pady=5)

    def make_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1

            if guess < self.number:
                self.result_label.config(text="🔵 Too low! Try again.")
            elif guess > self.number:
                self.result_label.config(text="🔴 Too high! Try again.")
            else:
                duration = time.time() - self.start_time
                self.result_label.config(
                    text=f"🎉 Correct! Number was {self.number}. Attempts: {self.attempts}, Time: {duration:.2f}s"
                )
                self.end_game()
                return

            if self.attempts >= self.max_attempts:
                self.result_label.config(text=f"😢 Game Over! The number was {self.number}.")
                self.end_game()

        except ValueError:
            self.result_label.config(text="⚠️ Please enter a valid number!")

    def end_game(self):
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.pack_forget()
        self.guess_button.pack_forget()

        play_again = tk.Button(
            self.root,
            text="🔁 Play Again",
            command=self.reset_game,
            bg="#000000",
            fg="black",
            font=("Arial", 13, "bold"),
            relief="raised",
            bd=3,
            width=15
        )
        play_again.pack(pady=15)

    def reset_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGame(root)
    root.mainloop()