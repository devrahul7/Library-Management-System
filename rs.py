import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

class LibraryLoginGUI:
    def __init__(self, master):
        self.master = master
        master.title("Library Management System - Login")
        master.geometry("400x300")
        master.configure(bg='#f0f0f0')

        # Custom font
        self.title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        self.label_font = tkFont.Font(family="Helvetica", size=10)
        self.button_font = tkFont.Font(family="Helvetica", size=10, weight="bold")

        # Title
        self.title_label = tk.Label(master, text="Library Management System", font=self.title_font, bg='#f0f0f0')
        self.title_label.pack(pady=20)

        # Username
        self.username_label = tk.Label(master, text="Username:", font=self.label_font, bg='#f0f0f0')
        self.username_label.pack()
        self.username_entry = tk.Entry(master, width=30)
        self.username_entry.pack(pady=5)

        # Password
        self.password_label = tk.Label(master, text="Password:", font=self.label_font, bg='#f0f0f0')
        self.password_label.pack()
        self.password_entry = tk.Entry(master, show="*", width=30)
        self.password_entry.pack(pady=5)

        # Login Button
        self.login_button = tk.Button(master, text="Login", command=self.login, font=self.button_font, bg='#4CAF50', fg='white', width=10)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Here you would typically check the username and password against a database
        # For this example, we'll use a hardcoded check
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome to the Library Management System!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    login_gui = LibraryLoginGUI(root)
    root.mainloop()