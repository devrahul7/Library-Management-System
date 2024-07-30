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


ISBN_Label = Label(text="ISBN",bg="#8AAAE5",font=("Bold Arial","15"))
ISBN_Label.place(x=230,y=180)

ISBN_Label_Entry= Entry(lb,width=15,font=('Arial 24'))
ISBN_Label_Entry.place(x=350,y=170)

Author_Label = Label(text="Author",bg="#8AAAE5",font=("Bold Arial","15"))
Author_Label.place(x=220,y=240)

Author_Entry= Entry(lb,width=15,font=('Arial 24'))
Author_Entry.place(x=350,y=230)

Date_Published = Label(text="Date Published",bg="#8AAAE5",font=("Bold Arial","15"))
Date_Published.place(x=180,y=300)

Date_Published_Entry = Entry(lb,width=15,font=('Arial 24'))
Date_Published_Entry.place(x=350,y=290)

Description_Name = Label(text="Description",bg="#8AAAE5",font=("Bold Arial","15"))
Description_Name.place(x=200,y=350)

#problemm in entry box
Description_Entry = Entry(lb,width=15,font=('Arial 24'))
Description_Entry.place(x=350,y=340)


def show_message_box():
    messagebox.showinfo("Library Management System", "Book Added Succesfully")
Button_Add_Book = Button(text="Add Book",font=('Arial'),command=show_message_box)
Button_Add_Book.place(x=350,y=500)


def show_message_box2():
    messagebox.showinfo("Library Management System", "Exited")
Button_Exit = Button(text="   Exit   ",font=('Arial'),command=show_message_box2)
Button_Exit.place(x=1100,y=500)        

mainloop()