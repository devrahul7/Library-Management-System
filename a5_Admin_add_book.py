from tkinter import *
from tkinter import messagebox
lb =Tk()  #creating a blank window
lb.title(" Library Management System ") #PROVIDING A TIITLE

lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") #here +100 or - 100 is used to replace window position
lb.config(bg="#8AAAE5")  #DEFINING BG COLOUR OF THE WINDOW
lb.state("zoomed")
colour1 = Label(text="Library Management System                                                                                                                                                                                              Add Book",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()

colour2 = Label(bg="#6D7ACF",width=240,height=3)
colour2.pack(side=BOTTOM)

Add_Book_Text = Label(text="Add Book",font=("Bold Arial","20"),bg="#8AAAE5")
Add_Book_Text.place(x=710,y=55)


Book_Name = Label(text="Book Name",bg="#8AAAE5",font=("Bold Arial","15"))
Book_Name.place(x=200,y=110)

Entry_Book_Name = Entry(lb,width=15,font=('Arial 24'))
Entry_Book_Name.place(x=350,y=110)


book_number_label = Label(text="Book Number",bg="#8AAAE5",font=("Bold Arial","15"))
book_number_label.place(x=200,y=180)
book_number_entry= Entry(lb,width=15,font=('Arial 24'))
book_number_entry.place(x=350,y=170)

Author_Label = Label(text="Author",bg="#8AAAE5",font=("Bold Arial","15"))
Author_Label.place(x=220,y=240)

Author_Entry= Entry(lb,width=15,font=('Arial 24'))
Author_Entry.place(x=350,y=230)

Date_Published = Label(text="Date Published",bg="#8AAAE5",font=("Bold Arial","15"))
Date_Published.place(x=180,y=300)

Date_Published_Entry = Entry(lb,width=15,font=('Arial 24'))
Date_Published_Entry.place(x=350,y=290)


def add_book_func():
    messagebox.showinfo("Library Management System", "Book Added Succesfully")
    lb.destroy()
    import a4_Admin_Dashboard
Button_Add_Book = Button(text="Add Book",font=('Arial'),command=add_book_func)
Button_Add_Book.place(x=150,y=600)

def Update_func():
    messagebox.showinfo("Library Management System", "Book Updated Succesfully")
    lb.destroy()
    import a4_Admin_Dashboard
Button_update_Book = Button(text="Update Book",font=('Arial'),command=Update_func)
Button_update_Book.place(x=300,y=600)


def Retrieve_fun():
    messagebox.showinfo("Library Management System", "Book Retrieved Succesfully")
    lb.destroy()
    import a4_Admin_Dashboard
Button_Retrieve_Book = Button(text="Retrieve Book",font=('Arial'),command=Retrieve_fun)
Button_Retrieve_Book.place(x=470,y=600)


def del_func():
    messagebox.showinfo("Library Management System", "Book Delete Succesfully")
    lb.destroy()
    import a4_Admin_Dashboard
Button_Delete_Book = Button(text="Delete Book",font=('Arial'),command=del_func)
Button_Delete_Book.place(x=650,y=600)




def exitfunc():
    messagebox.showinfo("Library Management System", "Exited")

    lb.destroy()  # Close the current window
    import a4_Admin_Dashboard

Button_Exit = Button(text="   Exit   ",font=('Arial'),command=exitfunc)
Button_Exit.place(x=1400,y=100)        


mainloop()