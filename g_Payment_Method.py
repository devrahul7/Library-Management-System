from tkinter import *

from tkinter import messagebox
lb =Tk()  #creating a blank window
lb.title(" Library Management System ") #PROVIDING A TIITLE

lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") #here +100 or - 100 is used to replace window position
lb.config(bg="#8AAAE5")  #DEFINING BG COLOUR OF THE WINDOW
lb.state("zoomed")
 
colour1 = Label(text="      Library Management System                                                                                                                                                                                   Payment Method",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)   #used for providing the colouring to the top and bottom side
colour2.pack(side=BOTTOM)

payment_label = Label(text="Payment Method",bg="#8AAAE5",font=("Bold Arial","17"),width=13,height=1)   #used for providing the colouring to the top and bottom side
payment_label.place(x=710,y=70)

Book_Label = Label(text="Book Name",font=("Bold Arial","20"),bg="#8AAAE5")
Book_Label.place(x=400,y=170)
bok_Entry_Name = Entry(lb,width=15,font=('Arial 20'))
bok_Entry_Name.place(x=570,y=170)

Book_Number_label = Label(text="Student ID",bg="#8AAAE5",font=("Bold Arial","20"))
Book_Number_label.place(x=400,y=225)
Book_Number_Entry= Entry(lb,width=15,font=('Arial 20'))
Book_Number_Entry.place(x=570,y=225)


Amount_Label= Label(text="Amount",bg="#8AAAE5",font=("Bold Arial","20"))
Amount_Label.place(x=400,y=280)
Amount_Entry = Entry(lb,width=15,font=('Arial 20'))
Amount_Entry.place(x=570,y=280)


pay_now_button = Button(text="Pay Now",font=('Arial'))
pay_now_button.place(x=350,y=500)


def show_message_box2():
    messagebox.showinfo("Library Management System", "Exited")
Button_Exit = Button(text="   Exit   ",font=('Arial'),command=show_message_box2)
Button_Exit.place(x=1100,y=500)   




mainloop()