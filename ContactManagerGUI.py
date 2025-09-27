import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

CONTACTS_FILE = "contacts.json"

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("📒 Contact Management System")
        self.root.geometry("600x500")
        self.root.configure(bg="#1e1e2f")

        # Title
        title = tk.Label(root, text="📒 Contact Management System", font=("Comic Sans MS", 18, "bold"), fg="#ffcc00", bg="#1e1e2f")
        title.pack(pady=10)

        # Frame for input fields
        form_frame = tk.Frame(root, bg="#1e1e2f")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Name:", font=("Arial", 12, "bold"), fg="white", bg="#1e1e2f").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        tk.Label(form_frame, text="Phone:", font=("Arial", 12, "bold"), fg="white", bg="#1e1e2f").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        tk.Label(form_frame, text="Email:", font=("Arial", 12, "bold"), fg="white", bg="#1e1e2f").grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()

        tk.Entry(form_frame, textvariable=self.name_var, font=("Arial", 12), width=25).grid(row=0, column=1, padx=5, pady=5)
        tk.Entry(form_frame, textvariable=self.phone_var, font=("Arial", 12), width=25).grid(row=1, column=1, padx=5, pady=5)
        tk.Entry(form_frame, textvariable=self.email_var, font=("Arial", 12), width=25).grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        btn_frame = tk.Frame(root, bg="#1e1e2f")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="➕ Add Contact", command=self.add_contact, bg="#00adb5", fg="white", font=("Arial", 12, "bold"), width=15).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="✏️ Edit Contact", command=self.edit_contact, bg="#f96d00", fg="white", font=("Arial", 12, "bold"), width=15).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="🗑️ Delete Contact", command=self.delete_contact, bg="#f05454", fg="white", font=("Arial", 12, "bold"), width=15).grid(row=0, column=2, padx=5)

        # Contact list (Treeview)
        self.tree = ttk.Treeview(root, columns=("Name", "Phone", "Email"), show="headings", height=10)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.pack(pady=10, fill="x")

        self.load_contacts()

    def add_contact(self):
        name, phone, email = self.name_var.get(), self.phone_var.get(), self.email_var.get()
        if name == "" or phone == "" or email == "":
            messagebox.showerror("Error", "All fields are required!")
            return
        self.tree.insert("", "end", values=(name, phone, email))
        self.save_contacts()
        self.clear_fields()

    def edit_contact(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a contact to edit!")
            return
        name, phone, email = self.name_var.get(), self.phone_var.get(), self.email_var.get()
        if name == "" or phone == "" or email == "":
            messagebox.showerror("Error", "All fields are required!")
            return
        self.tree.item(selected, values=(name, phone, email))
        self.save_contacts()
        self.clear_fields()

    def delete_contact(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a contact to delete!")
            return
        self.tree.delete(selected)
        self.save_contacts()

    def clear_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")

    def save_contacts(self):
        contacts = []
        for row in self.tree.get_children():
            contacts.append(self.tree.item(row)["values"])
        with open(CONTACTS_FILE, "w") as f:
            json.dump(contacts, f, indent=4)

    def load_contacts(self):
        if os.path.exists(CONTACTS_FILE):
            with open(CONTACTS_FILE, "r") as f:
                contacts = json.load(f)
                for contact in contacts:
                    self.tree.insert("", "end", values=contact)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
