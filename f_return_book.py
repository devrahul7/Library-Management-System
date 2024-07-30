from tkinter import *
from tkinter import messagebox
lb =Tk()  #creating a blank window
lb.title(" Library Management System ") #PROVIDING A TIITLE

lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") #here +100 or - 100 is used to replace window position
lb.config(bg="#8AAAE5")  #DEFINING BG COLOUR OF THE WINDOW
lb.state("zoomed")

colour1 = Label(text="Library Management System                                                                                                                                                                                           Return BooK",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)   #used for providing the colouring to the top and bottom side
colour2.pack(side=BOTTOM)


Return_Book_Text = Label(text="Return Book",font=("Bold Arial","20"),bg="#8AAAE5")
Return_Book_Text.place(x=710,y=55)



Name = Label(text="Name",bg="#8AAAE5",font=("Bold Arial","15"))
Name.place(x=270,y=110)
Entry_Name = Entry(lb,width=15,font=('Arial 24'))
Entry_Name.place(x=350,y=110)


Label_Your_name = Label(text="Issued Book Name",bg="#8AAAE5",font=("Bold Arial","15"))
Label_Your_name.place(x=160,y=180)
Your_Name_Entry= Entry(lb,width=15,font=('Arial 24'))
Your_Name_Entry.place(x=350,y=170)


Book_Name_Label = Label(text="Issued Book Number",bg="#8AAAE5",font=("Bold Arial","15"))
Book_Name_Label.place(x=140,y=240)
Book_Name_Entry= Entry(lb,width=15,font=('Arial 24'))
Book_Name_Entry.place(x=350,y=230)



Label_Date_Returned_ = Label(text="      Issued Date",bg="#8AAAE5",font=("Bold Arial","15"))
Label_Date_Returned_.place(x=180,y=300)
Label_Date_Returned_Entry = Entry(lb,width=15,font=('Arial 24'))
Label_Date_Returned_Entry.place(x=350,y=290)


def show_message_box():
    messagebox.showinfo("Library Management System", "Book Returned Succesfully")
Button_Return_Book = Button(text="Return Book",font=('Arial'),command=show_message_box)
Button_Return_Book.place(x=350,y=500)
#problemm in entry box

def show_message_box2():
    messagebox.showinfo("Library Management System", "Exited")
Button_Exit = Button(text="   Exit   ",font=('Arial'),command=show_message_box2)
Button_Exit.place(x=1100,y=500)   

mainloop()


 