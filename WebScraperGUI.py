import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv

class WebScraperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Web Scraper - Product Info")
        self.root.geometry("750x500")
        self.root.configure(bg="#1e1e2f")

        # Title
        tk.Label(root, text="🛒 Product Scraper", font=("Comic Sans MS", 18, "bold"), fg="#ffcc00", bg="#1e1e2f").pack(pady=10)

        # URL input
        frame = tk.Frame(root, bg="#1e1e2f")
        frame.pack(pady=5)
        tk.Label(frame, text="Enter URL:", font=("Arial", 12, "bold"), fg="white", bg="#1e1e2f").grid(row=0, column=0, padx=5)

        self.url_var = tk.StringVar(value="https://books.toscrape.com/catalogue/category/books_1/index.html")
        tk.Entry(frame, textvariable=self.url_var, font=("Arial", 12), width=50).grid(row=0, column=1, padx=5)

        # Buttons
        btn_frame = tk.Frame(root, bg="#1e1e2f")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="🔍 Scrape", command=self.scrape, bg="#00adb5", fg="white", font=("Arial", 12, "bold"), width=12).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="💾 Export CSV", command=self.export_csv, bg="#f96d00", fg="white", font=("Arial", 12, "bold"), width=12).grid(row=0, column=1, padx=10)

        # Treeview table
        self.tree = ttk.Treeview(root, columns=("Name", "Price", "Rating"), show="headings", height=15)
        self.tree.heading("Name", text="Product Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Rating", text="Rating")
        self.tree.pack(pady=10, fill="x")

        self.products = []

    def scrape(self):
        url = self.url_var.get()
        try:
            response = requests.get(url)
            if response.status_code != 200:
                messagebox.showerror("Error", f"Failed to fetch page: {response.status_code}")
                return

            soup = BeautifulSoup(response.text, "html.parser")
            items = soup.find_all("article", class_="product_pod")

            self.products = []
            for item in items:
                name = item.h3.a["title"]
                price = item.find("p", class_="price_color").text
                rating = item.p["class"][1] if len(item.p["class"]) > 1 else "No Rating"
                self.products.append([name, price, rating])

            # Update Treeview
            for row in self.tree.get_children():
                self.tree.delete(row)

            for prod in self.products:
                self.tree.insert("", "end", values=prod)

            messagebox.showinfo("Success", f"Scraped {len(self.products)} products successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def export_csv(self):
        if not self.products:
            messagebox.showerror("Error", "No data to export! Please scrape first.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            with open(file_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Product Name", "Price", "Rating"])
                writer.writerows(self.products)
            messagebox.showinfo("Exported", f"Data exported to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperGUI(root)
    root.mainloop()
