import tkinter as tk
from tkinter import messagebox

class LibrarySignupGUI:
    def __init__(self, master):
        self.master = master
        master.title("Library Management System")
        master.geometry("500x500")
        master.configure(bg='#B0C4DE')  # Light Steel Blue

        # Header
        self.header_frame = tk.Frame(master, bg='#6A5ACD', height=50)  # Slate Blue
        self.header_frame.pack(fill=tk.X)
        self.header_label = tk.Label(self.header_frame, text="Library Management System", 
                                     font=("Arial", 16), bg='#6A5ACD', fg='white')
        self.header_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.signup_link = tk.Label(self.header_frame, text="Signup now", 
                                    font=("Arial", 12), bg='#6A5ACD', fg='white')
        self.signup_link.pack(side=tk.RIGHT, padx=10, pady=10)

        # Main content
        self.content_frame = tk.Frame(master, bg='#B0C4DE')
        self.content_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Title
        self.title_label = tk.Label(self.content_frame, text="Sign Up Page", 
                                    font=("Arial", 18, "bold"), bg='#B0C4DE')
        self.title_label.pack(pady=10)

        # Input fields
        self.create_input_field("Name")
        self.create_input_field("Student Id")
        self.create_input_field("Date of Birth")
        self.create_input_field("Contact")
        self.create_input_field("Address")

        # Buttons
        self.button_frame = tk.Frame(self.content_frame, bg='#B0C4DE')
        self.button_frame.pack(pady=20)
        
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.exit_app, 
                                     width=10, bg='white')
        self.exit_button.pack(side=tk.LEFT, padx=10)
        
        self.signup_button = tk.Button(self.button_frame, text="Signup", command=self.signup, 
                                       width=10, bg='white')
        self.signup_button.pack(side=tk.LEFT, padx=10)

        # Footer
        self.footer_frame = tk.Frame(master, bg='#6A5ACD', height=30)
        self.footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

    def create_input_field(self, label_text):
        frame = tk.Frame(self.content_frame, bg='#B0C4DE')
        frame.pack(fill=tk.X, pady=5)
        label = tk.Label(frame, text=label_text, width=15, anchor='w', bg='#B0C4DE')
        label.pack(side=tk.LEFT)
        entry = tk.Entry(frame, width=30)
        entry.pack(side=tk.LEFT)

    def exit_app(self):
        self.master.quit()

    def signup(self):
        messagebox.showinfo("Sign Up", "Sign up functionality not implemented yet.")

if __name__ == "__main__":
    root = tk.Tk()
    signup_gui = LibrarySignupGUI(root)
    root.mainloop()