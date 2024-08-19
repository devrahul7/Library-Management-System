from tkinter import *

from tkinter import messagebox
lb =Tk()  #creating a blank window
lb.title(" Library Management System ") #PROVIDING A TIITLE

lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") 
lb.config(bg="#8AAAE5") 
lb.state("zoomed")
 
colour1 = Label(text="      Library Management System                                                                                                                                                                                   Payment Page",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)   #used for providing the colouring to the top and bottom side
colour2.pack(side=BOTTOM)

payment_label = Label(text="Payment Page",bg="#8AAAE5",font=("Bold Arial","17"),width=13,height=1) 
payment_label.place(x=710,y=70)

Book_Label = Label(text="Book Name",font=("Bold Arial","20"),bg="#8AAAE5")
Book_Label.place(x=40,y=170)
bok_Entry_Name = Entry(lb,width=15,font=('Arial 20'))
bok_Entry_Name.place(x=230,y=170)

Book_Number_label = Label(text="Book Number",bg="#8AAAE5",font=("Bold Arial","20"))
Book_Number_label.place(x=30,y=225)
Book_Number_Entry= Entry(lb,width=15,font=('Arial 20'))
Book_Number_Entry.place(x=230,y=225)


Amount_Label= Label(text="Fine Amount",bg="#8AAAE5",font=("Bold Arial","20"))
Amount_Label.place(x=40,y=280)
Amount_Entry = Entry(lb,width=15,font=('Arial 20'))
Amount_Entry.place(x=230,y=280)
def payfunc():
    messagebox.showinfo("Library Management System", "Payment Succesful")
    lb.destroy()
    import a8_user_Dashboard

pay_fine_button = Button(text="Pay Fine",font=('Arial'),command=payfunc)
pay_fine_button.place(x=350,y=500)


def exitfunc():
    messagebox.showinfo("Library Management System", "Exited")
    lb.destroy()
    import a8_user_Dashboard
Button_Exit = Button(text="   Exit   ",font=('Arial'),command=exitfunc)
Button_Exit.place(x=1100,y=500)   

mainloop()
