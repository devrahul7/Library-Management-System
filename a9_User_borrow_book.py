from tkinter import *
from tkinter import messagebox
lb =Tk()  #creating a blank window
lb.title(" Library Management System ") #PROVIDING A TIITLE

lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") #here +100 or - 100 is used to replace window position
lb.config(bg="#8AAAE5")  #DEFINING BG COLOUR OF THE WINDOW
lb.state("zoomed")
colour1 = Label(text="Library Management System                                                                                                                                                                                              Borrow Book",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()

colour2 = Label(bg="#6D7ACF",width=240,height=3)
colour2.pack(side=BOTTOM)

Add_Book_Text = Label(text="Borrow Book",font=("Bold Arial","20"),bg="#8AAAE5")
Add_Book_Text.place(x=710,y=55)



Book_Name = Label(text="Book Name",bg="#8AAAE5",font=("Bold Arial","15"))
Book_Name.place(x=210,y=210)
Entry_Book_Name = Entry(lb,width=15,font=('Arial 24'))
Entry_Book_Name.place(x=350,y=200)



book_number_label = Label(text="Book Number",bg="#8AAAE5",font=("Bold Arial","15"))
book_number_label.place(x=200,y=265)
book_number_entry= Entry(lb,width=15,font=('Arial 24'))
book_number_entry.place(x=350,y=260)


Date_Borrowed = Label(text="Date Borrowed",bg="#8AAAE5",font=("Bold Arial","15"))
Date_Borrowed.place(x=190,y=330)
Date_Borrowed_Entry = Entry(lb,width=15,font=('Arial 24'))
Date_Borrowed_Entry.place(x=350,y=320)


def show_message_box():
    messagebox.showinfo("Library Management System", "Book Borrowed Succesfully")
    lb.destroy()
    import a8_user_Dashboard
Button_borrow_Book = Button(text="Borrow Book",font=('Arial'),command=show_message_box)
Button_borrow_Book.place(x=350,y=500)


def show_message_box2():
    messagebox.showinfo("Library Management System", "Exited")

    lb.destroy()  # Close the current window
    import a8_user_Dashboard
Button_Exit = Button(text="   Exit   ",font=('Arial'),command=show_message_box2)
Button_Exit.place(x=1100,y=500)        


mainloop()

