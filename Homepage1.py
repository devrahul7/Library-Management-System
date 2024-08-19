from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import datetime
import sqlite3

#============================================================Window for home page=======================================
root = Tk()
root.title("Library Management System")
root.iconbitmap("l.ico")
root.geometry("700x700+100-100")
root.config(bg="#8AAAE5")
root.state("zoomed")

#===========================================================Function to define sign up window===========================
def open_signup_window():
    signup_window = Toplevel(root)
    signup_window.title("Library Management System - Signup")
    signup_window.iconbitmap("l.ico")
    signup_window.geometry("700x700+100-100")
    signup_window.config(bg="#8AAAE5")
    signup_window.state("zoomed")

    # ===================================Sign Up Page UI components
    colour1 = Label(signup_window, text="      Library Management System                                                                                                                                                                                       Signup now", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
    colour1.pack()
    colour2 = Label(signup_window, bg="#6D7ACF", width=240, height=3)
    colour2.pack(side=BOTTOM)

    Sign_Up_page = Label(signup_window, text="Signup Page", bg="#8AAAE5", font=("Bold Arial", "17"), width=13, height=1)
    Sign_Up_page.place(x=710, y=70)

    Label_Username = Label(signup_window, text="Username", bg="#8AAAE5", font=("Bold Arial", "20"))
    Label_Username.place(x=200, y=170)
    EntryUsername = Entry(signup_window, width=15, font=('Arial 20'))
    EntryUsername.place(x=350, y=170)

    date_of_birth_name = Label(signup_window, text="Date of Birth", bg="#8AAAE5", font=("Bold Arial", "20"))
    date_of_birth_name.place(x=180, y=225)
    Entry_date_of_birth = Entry(signup_window, width=15, font=('Arial 20'))
    Entry_date_of_birth.place(x=350, y=225)

    Contact_name = Label(signup_window, text="Contact", bg="#8AAAE5", font=("Bold Arial", "20"))
    Contact_name.place(x=230, y=280)
    Entry_contact = Entry(signup_window, width=15, font=('Arial 20'))
    Entry_contact.place(x=350, y=280)

    Addres_name = Label(signup_window, text="Address", bg="#8AAAE5", font=("Bold Arial", "20"))
    Addres_name.place(x=230, y=335)
    Addres_Entry = Entry(signup_window, width=15, font=('Arial 20'))
    Addres_Entry.place(x=350, y=335)

    Password_label = Label(signup_window, text="Password", bg="#8AAAE5", font=("Bold Arial", "20"))
    Password_label.place(x=230, y=390)
    Password_entry = Entry(signup_window, show="*", width=15, font=('Arial 20'))
    Password_entry.place(x=350, y=390)

    # ============================*****************************User type selection
    Role_label = Label(signup_window, text="Role", bg="#8AAAE5", font=("Bold Arial", "20"))
    Role_label.place(x=230, y=445)
    role_var = StringVar(value="user")
    Role_admin = Radiobutton(signup_window, text="Admin", variable=role_var, value="admin", bg="#8AAAE5", font=("Bold Arial", "20"))
    Role_admin.place(x=350, y=440)
    Role_user = Radiobutton(signup_window, text="User", variable=role_var, value="user", bg="#8AAAE5", font=("Bold Arial", "20"))
    Role_user.place(x=450, y=440)

    # =====================================================================Database connection and creation
    conn = sqlite3.connect('Library_management_system.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            dob TEXT NOT NULL,
            contact TEXT NOT NULL,
            address TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('admin', 'user'))
        )
    ''')
    conn.commit()
    #=============================Function to handle the data connection with database
    def signup():
        username = EntryUsername.get()
        dob = Entry_date_of_birth.get()
        contact = Entry_contact.get()
        address = Addres_Entry.get()
        password = Password_entry.get()
        role = role_var.get()
        
        if username and dob and contact and address and password:
            try:
                c.execute("SELECT COUNT(*) FROM users WHERE role='admin'")
                if role == "admin" and c.fetchone()[0] > 0:
                    messagebox.showerror("Error", "Admin account already exists")
                    return

                c.execute("INSERT INTO users (username, dob, contact, address, password, role) VALUES (?, ?, ?, ?, ?, ?)", 
                          (username, dob, contact, address, password, role))
                conn.commit()
                messagebox.showinfo("Library Management System", "Sign up successfully")
                signup_window.destroy()
                open_login_window()
                
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists")
                open_login_window.deiconify()
        else:
            messagebox.showerror("Error", "Please fill out all fields")
            signup_window.destroy()
            root.deiconofy()

    Sign_up_page_button = Button(signup_window, text="Signup", font=('Arial'), command=signup)
    Sign_up_page_button.place(x=350, y=500)
    #==================================Define the exit for sign up page
    def exit_app():
        signup_window.destroy()
        root.deiconify()

    Button_Exit = Button(signup_window, text="   Exit   ", font=('Arial'), command=exit_app)
    Button_Exit.place(x=1100, y=500)
#======================================================Toplevel Window for login page==============================
def open_login_window():
    login_window = Toplevel(root)
    login_window.title("Library Management System - Login")
    login_window.iconbitmap("l.ico")
    login_window.geometry("700x700+100-100")
    login_window.config(bg="#8AAAE5")
    login_window.state("zoomed")

    admin = Label(login_window, text="Library Login", font=("Bold Arial", "30"), bg="#8AAAE5", fg="#000000")
    admin.place(x=900, y=150)

    library_photo = Image.open("zbc.png")
    c = library_photo.resize((850, 690))
    r = ImageTk.PhotoImage(c)
    image1 = Label(login_window, image=r)
    image1.image = r  # ======================================Keep a reference to avoid garbage collection
    image1.place(x=0, y=50)

    colour1 = Label(login_window, text="    Library Management System", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
    colour1.pack()

    colour2 = Label(login_window, bg="#6D7ACF", width=240, height=3)
    colour2.pack(side=BOTTOM)

    def login():
        username = User_Entry.get()
        password = password_Entry.get()
        
        conn = sqlite3.connect("Library_management_system.db")
        c = conn.cursor()
        c.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        
        if result:
            role = result[0]
            if role == 'admin':
                messagebox.showinfo("Library Management System", "Welcome Admin!")
                login_window.destroy()
                open_admin_dashboard() # ********************************Redirect to the admin dashboard
            else:
                messagebox.showinfo("Library Management System", "Welcome User!")
                login_window.destroy()
                open_user_dashboard()  # ********************************Redirect to the user dashboard
        else:
            messagebox.showerror("Error", "Invalid credentials")

        conn.close()

    username = Label(login_window, text="Username", font="34", bg="#8AAAE5")
    username.place(x=900, y=270)

    password = Label(login_window, text="Password", font="34", bg="#8AAAE5", fg="black")
    password.place(x=900, y=360)

    log_inButton = Button(login_window, text="Login", font=("4"), fg="black", bg="white", command=login)
    log_inButton.place(x=900, y=550, height=35)

    def onclick(event, text):
        if event.widget.get() == text:
            event.widget.delete(0, END)
            event.widget.insert(0, '')

    def offclick(event, text):
        if event.widget.get() == '':
            event.widget.insert(0, text)

    
    
    def open_reset_password_window():
        reset_window = Toplevel(root)
        reset_window.state("zoomed")
        reset_window.title('Library Management System - Reset Password')
        reset_window.iconbitmap("l.ico")
        reset_window.geometry("700x700+100-100")
        reset_window.config(bg="#8AAAE5")
    
        colour1 = Label(reset_window, text="      Library Management System                                                                                                                                                                                   Reset Password", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
        colour1.pack()
        colour2 = Label(reset_window, bg="#6D7ACF", width=240, height=3)
        colour2.pack(side=BOTTOM)
    
        Label_reset_password = Label(reset_window, text="Reset Your Password?", font=("Arial Black", "25"), fg="blue", bg='#8AAAE5', width=50)
        Label_reset_password.pack(padx=20, pady=30)
    
        label_username = Label(reset_window, text="Username", font=("Arial", "20"), bg='#8AAAE5')
        label_username.place(x=150, y=170)
        username_Entry = Entry(reset_window, font=("Arial", "20"), fg="black", width=17)
        username_Entry.place(x=400, y=170)
    
        old_password = Label(reset_window, text="      Old Password", font=("Arial", "20"), bg='#8AAAE5')
        old_password.place(x=80, y=230)
        old_password_Entry = Entry(reset_window, font=("Arial", "20"), fg="black", width=17, show='*')
        old_password_Entry.place(x=400, y=230)
    
        type_new_password = Label(reset_window, text="Type New Password", font=("Arial", "20"), bg='#8AAAE5')
        type_new_password.place(x=80, y=290)
        type_new_password_Entry = Entry(reset_window, font=("Arial", "20"), fg="black", width=17, show='*')
        type_new_password_Entry.place(x=400, y=290)
    
        retype_password = Label(reset_window, text="  Retype password", bg='#8AAAE5', font=("Arial", "20"))
        retype_password.place(x=80, y=350)
        retype_Entry = Entry(reset_window, font=("Arial", "20"), width=17, show='*')
        retype_Entry.place(x=400, y=350)
    
        def confirm_fun():
            username = username_Entry.get()
            old_password = old_password_Entry.get()
            new_password = type_new_password_Entry.get()
            retype_password = retype_Entry.get()
            
            if username and old_password and new_password and retype_password:
                if new_password == retype_password:
                    conn = sqlite3.connect('Library_management_system.db')
                    c = conn.cursor()
                    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, old_password))
                    result = c.fetchone()
                    
                    if result:
                        c.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
                        conn.commit()
                        messagebox.showinfo("Library Management System", "Password Reset Successfully")
                        reset_window.destroy()  
                        login_window.deiconify()  #====================================== Redirect to the login window
                    else:
                        messagebox.showerror("Error", "Invalid username or old password")
                    conn.close()
                else:
                    messagebox.showerror("Error", "New password and retyped password do not match")
            else:
                messagebox.showerror("Error", "Please fill out all fields")
    
        confirm_button = Button(reset_window, text="Confirm", fg="green", bg="white", font=("Arial", "15"), width=8, command=confirm_fun)
        confirm_button.place(x=950, y=600)
    
        def exit_but():
            messagebox.showinfo("Library Management System", "Exited")
            reset_window.destroy()  
            login_window.deiconify()# ==================================================Redirect to the login window
    
        Exit_button = Button(reset_window, text="Exit", fg="red", bg="white", font=("Arial", "15"), width=8, command=exit_but)
        Exit_button.place(x=500, y=600)

    reset_Button = Button(login_window, text="Reset Password?", font=("4"), fg="black", bg="white", command=open_reset_password_window)
    reset_Button.place(x=1060, y=550, height=35)

    placeholder = 'Enter Username or Email'
    User_Entry = Entry(login_window, font="20", bg='white', fg="black")
    User_Entry.place(x=900, y=310, height=35, width=235)
    User_Entry.insert(0, placeholder)
    User_Entry.bind('<FocusIn>', lambda event, text=placeholder: onclick(event, text))
    User_Entry.bind('<FocusOut>', lambda event, text=placeholder: offclick(event, text))

    placeholder1 = 'Enter Password'
    password_Entry = Entry(login_window, font="20", show="*")
    password_Entry.place(x=900, y=397)
    password_Entry.insert(0, placeholder1)
    password_Entry.bind('<FocusIn>', lambda event, text=placeholder1: onclick(event, text))
    password_Entry.bind('<FocusOut>', lambda event, text=placeholder1: offclick(event, text))

    def add():
        if a.get() == 0:
            password_Entry.config(show="*")
        else:
            password_Entry.config(show="")

    a = IntVar()
    Show_Password_Button1 = Checkbutton(login_window, text="Show Password", variable=a, command=add, font="20")
    Show_Password_Button1.place(x=900, y=460)
       

colour1 = Label(text="    Library Management System                                                           Welcome to BookWarica Library",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)
colour2.pack(side=BOTTOM)

library_photo  = Image.open("y.png")
c=library_photo.resize((300,250))
r = ImageTk.PhotoImage(c)                
image1=Label(image=r,bg="#8AAAE5").pack()

name1 = Label(text="Library",font=("Arial Bold","20"),fg="#34A853",bg="#8AAAE5")
name1.place(x=600,y=200)

name2 = Label(text="Management",font=("Arial Bold","20"),fg="#FF7A00",bg="#8AAAE5")
name2.place(x=705,y=200)

name3 = Label(text="System",font=("Arial Bold","20"),fg="#34A853",bg="#8AAAE5")
name3.place(x=880,y=200)

label1 = Label(bg="#4285F4",height=3,width=100)
label1.place(x=440,y=245)

yet_name = Label(text="Don't have a account yet?",font=("Arial Bold","15"),fg="black",bg="#4285F4")
yet_name.place(x=450,y=258)

sign_up_button = Button(text="Sign up",font=("Arial Bold","10"),fg="black",bg="#4285F4",command=open_signup_window)
sign_up_button.place(x=1050,y=258)

introduction_label = Label(text="Introduction",font=("Arial Bold","20"),fg="#CC0000",bg="#8AAAE5")
introduction_label.place(x=700,y=320)

intRo_text =  Label(text="Libraries store the energy that fuels the imagination \n        They open up windows to the world and inspire us to explore and achieve,\n and contribute to improving our quality of life.",font=("Arial","15"),fg="black",bg="#8AAAE5")
intRo_text.place(x=440,y=360)

intRo_text2 =  Label(text="Nothing is pleasanter than exploring a library \n So for exploring more click Sign up/Sign in ",font=("Arial","15"),fg="black",bg="#8AAAE5")
intRo_text2.place(x=600,y=450)

btn_Sign_in = Button(text="Sign in",font=("Arial","15"),bg="#6D7ACF",command=open_login_window)
btn_Sign_in.place(x=1520,y=80,anchor="e")

Bottom_text = Label(text="BookWarica  LiBrarY",font=("Arial Bold","15"),fg="black",bg="#6D7ACF")
Bottom_text.place(x=680,y=750)




# ==========================================================Main application window to add member
def open_add_member_window():

    add_member_window = Toplevel()
    add_member_window.title("Library Management System")
    add_member_window.iconbitmap("l.ico")
    add_member_window.geometry("700x700+100-100")
    add_member_window.config(bg="#8AAAE5")
    add_member_window.state("zoomed")

    colour2 = Label(add_member_window, bg="#6D7ACF", width=240, height=3)
    colour2.pack(side=BOTTOM)

    Name_label = Label(add_member_window, text="Library Management System", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
    Name_label.pack()
    Admin_member = Label(add_member_window, text="ADD MEMBER", font=("Arial Black", "20"), fg="black", bg='#8AAAE5', width=50)
    Admin_member.place(x=280, y=60)
    
    #  ****************************************************Window widgets of members
    

    Label_Full_Name = Label(add_member_window, text="Full Name", bg="#8AAAE5", font=("Bold Arial", 15))
    Label_Full_Name.place(x=200, y=110)
    Entry_Label_Full_Name = Entry(add_member_window, width=15, font=('Arial', 24))
    Entry_Label_Full_Name.place(x=350, y=110)

    Label_Username = Label(add_member_window, text="Username", bg="#8AAAE5", font=("Bold Arial", 15))
    Label_Username.place(x=200, y=180)
    Entry_Label_Username = Entry(add_member_window, width=15, font=('Arial', 24))
    Entry_Label_Username.place(x=350, y=170)

    Label_Email  = Label(add_member_window, text="Email", bg="#8AAAE5", font=("Bold Arial", 15))
    Label_Email .place(x=220, y=240)
    Entry_Label_Email = Entry(add_member_window, width=15, font=('Arial', 24))
    Entry_Label_Email.place(x=350, y=230)

    Label_Phone_number = Label(add_member_window, text="Phone No", bg="#8AAAE5", font=("Bold Arial", 15))
    Label_Phone_number.place(x=180, y=300)
    Entry_Label_Phone_number = Entry(add_member_window, width=15, font=('Arial', 24))
    Entry_Label_Phone_number.place(x=350, y=290)
    
    
    
    # ==============================================================Database connection
    conn = sqlite3.connect('Library_management_system.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS members (
                    id INTEGER PRIMARY KEY,
                    full_name TEXT,
                    username TEXT,
                    email TEXT,
                    phone_number TEXT)''')
    conn.commit()
    conn.close()
    
    def add_member_to_db():
        full_name = Entry_Label_Full_Name.get()
        username = Entry_Label_Username.get()
        email = Entry_Label_Email.get()
        phone_number = Entry_Label_Phone_number.get()

        if not full_name or not username or not email or not phone_number:
            messagebox.showerror("Library Management System", "Please fill in all fields")
            return
        
        conn = sqlite3.connect('Library_management_system.db')
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO members (full_name, username, email, phone_number) VALUES (?, ?, ?, ?)",
                       (full_name, username, email, phone_number))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Library Management System", "Member Added Successfully")
        open_admin_dashboard()

    
    def retrieve_member_to_db():
        username = Entry_Label_Username.get()
        
        conn = sqlite3.connect('Library_management_system.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM members WHERE username=?", (username,))
        member = cursor.fetchone()
        conn.close()
        
        if member:
            Entry_Label_Full_Name.delete(0, END)
            Entry_Label_Full_Name.insert(0, member[1])
            Entry_Label_Email.delete(0, END)
            Entry_Label_Email.insert(0, member[3])
            Entry_Label_Phone_number.delete(0, END)
            Entry_Label_Phone_number.insert(0, member[4])
            messagebox.showinfo("Library Management System", "Member Retrieved Successfully")
        else:
            messagebox.showerror("Library Management System", "Member Not Found")
            add_member_window.destroy()
            open_admin_dashboard()
    
    def del_member():
        username = Entry_Label_Username.get()
        
        conn = sqlite3.connect('Library_management_system.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM members WHERE username=?", (username,))
        member = cursor.fetchone()
        
        if member:
            cursor.execute("DELETE FROM members WHERE username=?", (username,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Library Management System", "Member Deleted Successfully")
            add_member_window.destroy()
            open_admin_dashboard()
        else:
            conn.close()
            messagebox.showerror("Library Management System", "Member Not Found")
            add_member_window.destroy()
            open_admin_dashboard()
    
    Button_Add_Book = Button(add_member_window, text="Add Member", font=('Arial'), command=add_member_to_db)
    Button_Add_Book.place(x=150, y=600)

    Button_Retrieve_Book = Button(add_member_window, text="Retrieve Member", font=('Arial'), command=retrieve_member_to_db)
    Button_Retrieve_Book.place(x=350, y=600)

    Button_Delete_Book = Button(add_member_window, text="Delete Member", font=('Arial'), command=del_member)
    Button_Delete_Book.place(x=550, y=600)

    

    Button_Exit = Button(add_member_window, text="Exit", font=('Arial'), command=add_member_window.destroy)
    Button_Exit.place(x=1150, y=600)




#=====================================Toplevel window to display a book list
def open_book_list_window():
    book_list_window = Toplevel()
    book_list_window.title("Book List")
    book_list_window.geometry("800x600")
    book_list_window.config(bg="#8AAAE5")
    book_list_window.state("zoomed")

    colour2 = Label(book_list_window, bg="#6D7ACF", width=240, height=3)
    colour2.pack(side=BOTTOM)

    Name_label = Label(book_list_window, text="Library Management System", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
    Name_label.pack()
    Admin_book = Label(book_list_window, text="BOOK LIST", font=("Arial Black", "20"), fg="black", bg='#8AAAE5', width=50)
    Admin_book.place(x=280, y=60)

    def fetch_books():
        conn = sqlite3.connect('Library_management_system.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        return books

    def update_tree_view():
        for row in tree.get_children():
            tree.delete(row)
        books = fetch_books()
        for book in books:
            tree.insert("", END, values=book)

    def search_book():
        book_number = search_entry.get()
        conn = sqlite3.connect('Library_management_system.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE book_number=?", (book_number,))
        book = cursor.fetchone()
        conn.close()
        for row in tree.get_children():
            tree.delete(row)
        if book:
            tree.insert("", END, values=book)
        else:
            messagebox.showerror("Library Management System", "Book Not Found")

    def exit_book_list():
        book_list_window.destroy()
        open_admin_dashboard()

    # ******************************************************Book List Window widgets
    Label(book_list_window, text="BOOK LIST", font=("Bold ", 20), bg="#8AAAE5").pack(pady=50)

    search_frame = Frame(book_list_window, bg="#8AAAE5")
    search_frame.pack(pady=10)
    
    search_label = Label(search_frame, text="Book Number:", bg="#8AAAE5", font=("Arial", 15))
    search_label.pack(side=LEFT, padx=5)
    
    search_entry = Entry(search_frame, width=20, font=('Arial', 15))
    search_entry.pack(side=LEFT, padx=5)
    
    search_button = Button(search_frame, text="Search", command=search_book, font=('Arial', 15))
    search_button.pack(side=LEFT, padx=5)

    tree = ttk.Treeview(book_list_window, columns=("Book Name", "Book Number", "Author", "Date Published"), show='headings')
    tree.heading("Book Name", text="Book Name")
    tree.heading("Book Number", text="Book Number")
    tree.heading("Author", text="Author")
    tree.heading("Date Published", text="Date Published")
    tree.pack(pady=20)


    update_tree_view()

    exit_button = Button(book_list_window, text="Exit", command=exit_book_list, font=('Arial', 15))
    exit_button.pack(pady=10)

#=======================================================Function to define the window for add book===========================
def add_book_window():
    #===============================================Create a new Toplevel window to add book
    add_book_win = Toplevel()
    add_book_win.title("Manage Books")
    add_book_win.geometry("700x700+100-100")
    add_book_win.config(bg="#8AAAE5")
    add_book_win.state("zoomed")
    
    
    colour2 = Label(add_book_win, bg="#6D7ACF", width=240, height=3)
    colour2.pack(side=BOTTOM)

    Name_label = Label(add_book_win, text="Library Management System", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
    Name_label.pack()
    Admin_book = Label(add_book_win, text="ADMIN BOOK", font=("Arial Black", "20"), fg="black", bg='#8AAAE5', width=50)
    Admin_book.place(x=280, y=60)
    #  ****************************************************Window widgets of book

    Entry_Label_Full_Name = Label(add_book_win, text="Book Name", bg="#8AAAE5", font=("Bold Arial", 15))
    Entry_Label_Full_Name.place(x=200, y=110)

    Entry_Entry_Label_Full_Name = Entry(add_book_win, width=15, font=('Arial', 14))
    Entry_Entry_Label_Full_Name.place(x=350, y=110)

    Entry_Label_Username = Label(add_book_win, text="Book Number", bg="#8AAAE5", font=("Bold Arial", 15))
    Entry_Label_Username.place(x=200, y=180)
    book_number_entry = Entry(add_book_win, width=15, font=('Arial', 14))
    book_number_entry.place(x=350, y=170)

    Author_Label = Label(add_book_win, text="Author", bg="#8AAAE5", font=("Bold Arial", 15))
    Author_Label.place(x=220, y=240)

    Entry_Label_Email = Entry(add_book_win, width=15, font=('Arial', 14))
    Entry_Label_Email.place(x=350, y=230)

    Date_Published = Label(add_book_win, text="Date Published", bg="#8AAAE5", font=("Bold Arial", 15))
    Date_Published.place(x=180, y=300)

    Entry_Label_Phone_number = Entry(add_book_win, width=15, font=('Arial', 14))
    Entry_Label_Phone_number.place(x=350, y=290)


    conn = sqlite3.connect('Library_management_system.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            Entry_Label_Full_Name TEXT NOT NULL,
            book_number TEXT PRIMARY KEY,
            author TEXT NOT NULL,
            date_published TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

    def add_book_to_db():
        Entry_Label_Full_Name = Entry_Entry_Label_Full_Name.get()
        book_number = book_number_entry.get()
        author = Entry_Label_Email.get()
        date_published = Entry_Label_Phone_number.get()

        if not Entry_Label_Full_Name or not book_number or not author or not date_published:
            messagebox.showerror("Library Management System", "Please fill in all fields")

            open_admin_dashboard.deiconify()


        
        conn = sqlite3.connect('Library_management_system.db')
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO books (Entry_Label_Full_Name, book_number, author, date_published) VALUES (?, ?, ?, ?)",
                       (Entry_Label_Full_Name, book_number, author, date_published))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Library Management System", "Book Added Successfully")
        open_admin_dashboard()

    def update_book_in_db():
        Entry_Label_Full_Name = Entry_Entry_Label_Full_Name.get()
        book_number = book_number_entry.get()
        author = Entry_Label_Email.get()
        date_published = Entry_Label_Phone_number.get()
        
        conn = sqlite3.connect('Library_management_system.db')
        cursor = conn.cursor()
        
        cursor.execute("UPDATE books SET Entry_Label_Full_Name=?, author=?, date_published=? WHERE book_number=?",
                       (Entry_Label_Full_Name, author, date_published, book_number))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Library Management System", "Book Updated Successfully")
        add_book_win.destroy()
        open_admin_dashboard()

    def retrieve_book_from_db():
        book_number = book_number_entry.get()
        
        conn = sqlite3.connect('Library_management_system.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM books WHERE book_number=?", (book_number,))
        book = cursor.fetchone()
        conn.close()
        
        if book:
            Entry_Entry_Label_Full_Name.delete(0, END)
            Entry_Entry_Label_Full_Name.insert(0, book[0])
            Entry_Label_Email.delete(0, END)
            Entry_Label_Email.insert(0, book[2])
            Entry_Label_Phone_number.delete(0, END)
            Entry_Label_Phone_number.insert(0, book[3])
            messagebox.showinfo("Library Management System", "Book Retrieved Successfully")
        else:
            messagebox.showerror("Library Management System", "Book Not Found")

    def delete_book_from_db():
        book_number = book_number_entry.get()
        
        conn = sqlite3.connect('Library_management_system.db')
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM books WHERE book_number=?", (book_number,))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Library Management System", "Book Deleted Successfully")
        add_book_win.destroy()
        open_admin_dashboard()



    Button_Add_Book = Button(add_book_win, text="Add Book", font=('Arial'), command=add_book_to_db)
    Button_Add_Book.place(x=150, y=600)

    Button_Update_Book = Button(add_book_win, text="Update Book", font=('Arial'), command=update_book_in_db)
    Button_Update_Book.place(x=350, y=600)

    Button_Retrieve_Book = Button(add_book_win, text="Retrieve Book", font=('Arial'), command=retrieve_book_from_db)
    Button_Retrieve_Book.place(x=550, y=600)

    Button_Delete_Book = Button(add_book_win, text="Delete Book", font=('Arial'), command=delete_book_from_db)
    Button_Delete_Book.place(x=750, y=600)

    Button_view_member = Button(add_book_win,text='View Book',font=('Arial'),command=open_book_list_window)
    Button_view_member.place(x=950,y=600)

    Button_Exit = Button(add_book_win, text="Exit", font=('Arial'), command=add_book_win.destroy)
    Button_Exit.place(x=1150, y=600)

    

#=================================================           Function to open admin dashboard           ==========================
def open_admin_dashboard():
    admin_dashboard = Toplevel(root)
    admin_dashboard.title("Admin Dashboard")
    admin_dashboard.geometry("700x700")
    admin_dashboard.config(bg="#8AAAE5")
    admin_dashboard.iconbitmap("l.ico")

    colour2 = Label(admin_dashboard, bg="#6D7ACF", width=240, height=3)
    colour2.pack(side=BOTTOM)

    Name_label = Label(admin_dashboard, text="Library Management System", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
    Name_label.pack()
    Admin_Dasboard = Label(admin_dashboard, text="ADMIN DASHBOARD", font=("Arial Black", "20"), fg="black", bg='#8AAAE5', width=50)
    Admin_Dasboard.place(x=280, y=60)

    
    Add_Book_Button = Button(admin_dashboard, text="    +Add Book    ", bg="white", font="50", command=add_book_window)
    Add_Book_Button.place(x=100, y=220)



    BookList_Button = Button(admin_dashboard, text="     Book List      ", bg="white", font="50", command=open_book_list_window)
    BookList_Button.place(x=100, y=280)

        

    Add_Member_Button = Button(admin_dashboard, text="  +Add Member ", bg="white", font="50", command=open_add_member_window)
    Add_Member_Button.place(x=100, y=340)

    def logout():
        messagebox.showinfo("Library Management System", "Log Out Successfully")
        admin_dashboard.destroy()
        root.deiconify()

    logout_button = Button(admin_dashboard, text="Log Out", fg="red", bg="white", font=("Arial", "15"), width=8, command=logout)
    logout_button.place(x=1050, y=450)

    frame1 = Frame(admin_dashboard, bg="#7fa5e8", height=220, width=1600)
    frame1.place(x=0, y=520)

    Enquiry_ = Label(frame1, text="Enquiries:", font=("Arial", "15"), bg="#7fa5e8")
    Enquiry_.place(x=15, y=523)

    Email_id = Label(frame1, text="Email: bookwarica7@gmail.com", font=("Arial", "15"), bg="#7fa5e8")
    Email_id.place(x=15, y=580)

    Contact = Label(frame1, text="Contact: +977 9742869215", font=("Arial", "15"), bg="#7fa5e8")
    Contact.place(x=15, y=610)

    admin_dashboard.state('zoomed')


#=======================================================Window to work a payment methode=============


def open_payment_window():
    payment_window = Toplevel()
    payment_window.title("Library Management System - Payment")
    payment_window.iconbitmap("l.ico")
    payment_window.geometry("700x700+100-100")
    payment_window.config(bg="#8AAAE5")
    payment_window.state("zoomed")

    colour1 = Label(payment_window, text="      Library Management System                                                                                                                                                                                   Payment Page", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
    colour1.pack()
    colour2 = Label(payment_window, bg="#6D7ACF", width=240, height=3)
    colour2.pack(side=BOTTOM)

    payment_label = Label(payment_window, text="Payment Page", bg="#8AAAE5", font=("Bold Arial", "17"), width=13, height=1)
    payment_label.place(x=710, y=70)

    Book_Label = Label(payment_window, text="Book Name", font=("Bold Arial", "20"), bg="#8AAAE5")
    Book_Label.place(x=40, y=170)
    bok_Entry_Name = Entry(payment_window, width=15, font=('Arial 20'))
    bok_Entry_Name.place(x=230, y=170)

    Book_Number_label = Label(payment_window, text="Book Number", bg="#8AAAE5", font=("Bold Arial", "20"))
    Book_Number_label.place(x=30, y=225)
    Book_Number_Entry = Entry(payment_window, width=15, font=('Arial 20'))
    Book_Number_Entry.place(x=230, y=225)

    Amount_Label = Label(payment_window, text="Fine Amount", bg="#8AAAE5", font=("Bold Arial", "20"))
    Amount_Label.place(x=40, y=280)
    Amount_Entry = Entry(payment_window, width=15, font=('Arial 20'))
    Amount_Entry.place(x=230, y=280)

    Clear_fine = Label(payment_window, text="Cleared Date", bg="#8AAAE5", font=("Bold Arial", "20"))
    Clear_fine.place(x=40, y=345)
    Clear_fine_Ent = Entry(payment_window, width=15, font=('Arial 20'))
    Clear_fine_Ent.place(x=230, y=345)

    def payfunc():
        book_name = bok_Entry_Name.get()
        book_number = Book_Number_Entry.get()
        cleared_date = Clear_fine_Ent.get()

        
        conn = sqlite3.connect('Library_management_system.db')
        c = conn.cursor()

        # ******************************************Fetch the due date for the borrowed book
        c.execute("SELECT due_date FROM user_borrowed_books WHERE book_number=?", (book_number,))
        due_date_str = c.fetchone()
        if due_date_str:
            due_date = datetime.datetime.strptime(due_date_str[0], '%Y-%m-%d').date()
            today = datetime.date.today()
            if today > due_date:
                days_late = (today - due_date).days
                fine_amount = days_late * 0.569  # *************************************Assuming a fine of $0.569 per day
                Amount_Entry.insert(0, str(fine_amount))
                messagebox.showinfo("Library Management System", f"You are {days_late} days late. Please pay the fine of ${fine_amount:.2f}")

                #****************************** Add the book back to the admin's book list
                c.execute("INSERT INTO books (Entry_Label_Full_Name, book_number, author, date_published) VALUES (?, ?, ?, ?)", (book_name, book_number, "Unknown", "Unknown"))
                conn.commit()

                # ************************************Remove the book from the user's borrowed book table
                c.execute("DELETE FROM user_borrowed_books WHERE book_number=?", (book_number,))
                conn.commit()

                messagebox.showinfo("Library Management System", "Payment Successful. Book returned to the library.")
                payment_window.destroy()
                open_user_dashboard()
            else:
                days_remaining = (due_date - today).days
                messagebox.showinfo("Library Management System", f"{days_remaining} days remaining before the due date.")
        else:
            messagebox.showerror("Library Management System", "Book not found in the borrowed books list.")

        conn.close()

    pay_fine_button = Button(payment_window, text="Pay Fine", font=('Arial'), command=payfunc)
    pay_fine_button.place(x=350, y=500)

    def exitfunc():
        messagebox.showinfo("Library Management System", "Exited")
        payment_window.destroy()
        open_user_dashboard()

    Button_Exit = Button(payment_window, text="   Exit   ", font=('Arial'), command=exitfunc)
    Button_Exit.place(x=1100, y=500)

    def fine_treeview():
        fine_details_window = Toplevel(payment_window)
        fine_details_window.title("Library Management System - Fine Details")
        fine_details_window.iconbitmap("l.ico")
        fine_details_window.geometry("700x700+100-100")
        fine_details_window.config(bg="#8AAAE5")
        fine_details_window.state("zoomed")

        colour1 = Label(fine_details_window, text="      Library Management System                                                                                                                                                                                   Fine Details", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
        colour1.pack()
        colour2 = Label(fine_details_window, bg="#6D7ACF", width=240, height=3)
        colour2.pack(side=BOTTOM)

        fine_details_label = Label(fine_details_window, text="Fine Details", bg="#8AAAE5", font=("Bold Arial", "17"), width=13, height=1)
        fine_details_label.place(x=710, y=70)

        tree = ttk.Treeview(fine_details_window, columns=("Book Name", "Book Number", "Fine Amount", "Cleared Date"), show='headings')
        tree.heading("Book Name", text="Book Name")
        tree.heading("Book Number", text="Book Number")
        tree.heading("Fine Amount", text="Fine Amount")
        tree.heading("Cleared Date", text="Cleared Date")
        tree.pack(pady=20)


        conn = sqlite3.connect('Library_management_system.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS members (
                        id INTEGER PRIMARY KEY,
                        full_name TEXT,
                        username TEXT,
                        email TEXT,
                        phone_number TEXT)''')
        conn.commit()
        conn.close()

        # =================================================Fetch the fine details from the database
        conn = sqlite3.connect('Library_management_system.db')
        c = conn.cursor()
        c.execute("SELECT book_name, book_number, Amount_Entry.get(), Clear_fine_Ent.get() FROM user_borrowed_books WHERE book_number=?", (Book_Number_Entry.get(),))
        fine_details = c.fetchall()
        conn.close()

        for row in fine_details:
            tree.insert("", END, values=row)

        if fine_details:
            paid_label = Label(fine_details_window, text="SUCCESSFULLY PAID", font=("Arial Bold", 20), fg="green", bg="#8AAAE5")
            paid_label.place(x=500, y=500)

        def exit_fine_details():
            fine_details_window.destroy()
            payment_window.deiconify()

        exit_button = Button(fine_details_window, text="Exit", font=('Arial'), command=exit_fine_details)
        exit_button.pack(pady=10)

        

    Button_fine = Button(payment_window, text=" Fine Details", font=("Arial"), command=fine_treeview)
    Button_fine.place(x=650, y=500)




#=======================================================Function to open Borrow book window and it's respective functionalities====

def open_borrow_book_window():
    borrow_book_window = Toplevel()
    borrow_book_window.title("Library Management System - Borrow Book")
    borrow_book_window.iconbitmap("l.ico")
    borrow_book_window.geometry("700x700+100-100")
    borrow_book_window.config(bg="#8AAAE5")
    borrow_book_window.state("zoomed")

    colour1 = Label(borrow_book_window, text="Library Management System                                                                                                                                                                                              Borrow Book", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
    colour1.pack()

    colour2 = Label(borrow_book_window, bg="#6D7ACF", width=240, height=3)
    colour2.pack(side=BOTTOM)

    Add_Book_Text = Label(borrow_book_window, text="Borrow Book", font=("Bold Arial", "20"), bg="#8AAAE5")
    Add_Book_Text.place(x=710, y=55)

    Book_Name = Label(borrow_book_window, text="Book Name", bg="#8AAAE5", font=("Bold Arial", "15"))
    Book_Name.place(x=210, y=210)
    Entry_Book_Name = Entry(borrow_book_window, width=15, font=('Arial 24'))
    Entry_Book_Name.place(x=350, y=200)

    book_number_label = Label(borrow_book_window, text="Book Number", bg="#8AAAE5", font=("Bold Arial", "15"))
    book_number_label.place(x=200, y=265)
    book_number_entry = Entry(borrow_book_window, width=15, font=('Arial 24'))
    book_number_entry.place(x=350, y=260)

    Date_Borrowed = Label(borrow_book_window, text="Due  Date", bg="#8AAAE5", font=("Bold Arial", "15"))
    Date_Borrowed.place(x=190, y=330)
    Due_Date_Entry = Entry(borrow_book_window, width=15, font=('Arial 24'))
    Due_Date_Entry.place(x=350, y=320)

    def borrow_book():
        book_name = Entry_Book_Name.get()
        book_number = book_number_entry.get()
        due_date = Due_Date_Entry.get()

        
        conn = sqlite3.connect('Library_management_system.db')
        c = conn.cursor()

        # ***************************************************************Check if the book exists in the admin book list
        c.execute("SELECT * FROM books WHERE book_number=?", (book_number,))
        book_data = c.fetchone()
        if book_data:
            # ***********************************************************Remove the book from the admin book list
            c.execute("DELETE FROM books WHERE book_number=?", (book_number,))
            conn.commit()

            # ************************************************************Add the borrowed book to the user's borrowed book table
            c.execute("CREATE TABLE IF NOT EXISTS user_borrowed_books (id INTEGER PRIMARY KEY, book_name TEXT, book_number TEXT, due_date TEXT)")
            c.execute("INSERT INTO user_borrowed_books (book_name, book_number, due_date) VALUES (?, ?, ?)", (book_name, book_number, due_date))
            conn.commit()

            messagebox.showinfo("Library Management System", "Book Borrowed Successfully")
            borrow_book_window.destroy()
            open_user_dashboard()
        else:
            messagebox.showerror("Library Management System", "Book not found in the library")

        conn.close()

    Button_borrow_Book = Button(borrow_book_window, text="Borrow Book", font=('Arial'), command=borrow_book)
    Button_borrow_Book.place(x=350, y=500)

    def exit_func():
        messagebox.showinfo("Library Management System", "Exited")
        borrow_book_window.destroy()
        open_user_dashboard()

    Button_Exit = Button(borrow_book_window, text="   Exit   ", font=('Arial'), command=exit_func)
    Button_Exit.place(x=1100, y=500)


def open_user_dashboard():
    # ==================================================Create the Toplevel user dashboard window=========================
    user_dashboard_window = Toplevel(root)
    user_dashboard_window.geometry("700x700")
    user_dashboard_window.title("Library Management System")
    user_dashboard_window.config(bg="#8AAAE5")
    user_dashboard_window.iconbitmap("l.ico")
    user_dashboard_window.state("zoomed")

    # ==================================================Add header labels
    colour1 = Label(user_dashboard_window, text="      Library Management System ", font="(Helvetica,60)", anchor="w", bg="#6D7ACF", width=240, height=2)
    colour1.pack()

    colour2 = Label(user_dashboard_window, bg="#6D7ACF", width=240, height=3)
    colour2.pack(side=BOTTOM)
    
    User_Dashboard = Label(user_dashboard_window, text="USER DASHBOARD", font=("Arial Black", 20), fg="black", bg='#8AAAE5', width=50)
    User_Dashboard.place(x=280, y=60)

    

    Borrow_Book_Button = Button(user_dashboard_window, text="    Borrow Book    ", bg="white", font="50", command=open_borrow_book_window)
    Borrow_Book_Button.place(x=60, y=140)

    

    payment_Button = Button(user_dashboard_window, text="       Payment       ", bg="white", font="50", command=open_payment_window)
    payment_Button.place(x=60, y=200)

    def log_outf():
        user_dashboard_window.destroy()
        root.deiconify()

    exit_but = Button(user_dashboard_window, text="  Log out ", bg="white", fg="red", font="50", width=8, command=log_outf)
    exit_but.place(x=1050, y=450)

# =============================================Add buttom frame for contact information
    frame1 = Frame(user_dashboard_window, bg="#7fa5e8", height=220, width=1600)
    frame1.place(x=0, y=520)
    Enquiry_ = Label(frame1, text="Enquiries:", font=("Arial", 15), bg="#7fa5e8")
    Enquiry_.place(x=15, y=523)
    Email_id = Label(frame1, text="Email: bookwarica7@gmail.com", font=("Arial", 15), bg="#7fa5e8")
    Email_id.place(x=15, y=580)
    
    Contact = Label(frame1, text="Contact: +977 9742869215", font=("Arial", 15), bg="#7fa5e8")
    Contact.place(x=15, y=610)

mainloop()
