import tkinter as tk
from tkinter import ttk

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("🌡️ Temperature Converter")
        self.root.geometry("420x400")
        self.root.configure(bg="#1e1e2f")

        # Title
        self.title_label = tk.Label(
            root,
            text="🌡️ Advanced Temperature Converter",
            font=("Comic Sans MS", 16, "bold"),
            fg="#ffcc00",
            bg="#1e1e2f"
        )
        self.title_label.pack(pady=15)

        # Input field
        self.input_label = tk.Label(
            root,
            text="Enter Temperature:",
            font=("Arial", 12, "bold"),
            fg="#d5c6c6",
            bg="#1e1e2f"
        )
        self.input_label.pack(pady=5)

        self.temp_entry = tk.Entry(root, font=("Arial", 13), justify="center", bg="#000000")
        self.temp_entry.pack(pady=5)

        # Unit selection dropdown
        self.unit_label = tk.Label(
            root,
            text="Select Unit:",
            font=("Arial", 12, "bold"),
            fg="#060101",
            bg="#1e1e2f"
        )
        self.unit_label.pack(pady=5)

        self.unit_var = tk.StringVar(value="Celsius")
        self.unit_dropdown = ttk.Combobox(
            root,
            textvariable=self.unit_var,
            values=["Celsius", "Fahrenheit", "Kelvin"],
            state="readonly",
            font=("Arial", 12)
        )
        self.unit_dropdown.pack(pady=5)

        # Convert button
        self.convert_button = tk.Button(
            root,
            text="🔄 Convert",
            command=self.convert_temperature,
            bg="#00adb5",
            fg="white",
            font=("Arial", 13, "bold"),
            relief="raised",
            bd=3,
            width=15
        )
        self.convert_button.pack(pady=15)

        # Result labels
        self.result_label = tk.Label(
            root,
            text="",
            font=("Arial", 12, "bold"),
            fg="#eeeeee",
            bg="#1e1e2f"
        )
        self.result_label.pack(pady=10)

    def convert_temperature(self):
        try:
            temp = float(self.temp_entry.get())
            unit = self.unit_var.get()

            if unit == "Celsius":
                f = (temp * 9/5) + 32
                k = temp + 273.15
                result = f"{temp} °C = {f:.2f} °F | {k:.2f} K"
            elif unit == "Fahrenheit":
                c = (temp - 32) * 5/9
                k = (temp - 32) * 5/9 + 273.15
                result = f"{temp} °F = {c:.2f} °C | {k:.2f} K"
            else:  # Kelvin
                c = temp - 273.15
                f = (temp - 273.15) * 9/5 + 32
                result = f"{temp} K = {c:.2f} °C | {f:.2f} °F"

            self.result_label.config(text=result, fg="#00ff99")
        except ValueError:
            self.result_label.config(text="⚠️ Please enter a valid number!", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()