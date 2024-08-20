from tkinter import *
from tkinter import messagebox
lb = Tk()

lb.geometry("700x700")
lb.title(" Library Management System ") #PROVIDING A TIITLE
lb.config(bg="#8AAAE5") 
lb.iconbitmap("l.ico")


colour1 = Label(text="      Library Management System ",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)   #used for providing the colouring to the top and bottom side
colour2.pack(side=BOTTOM)
User_Dasboard = Label(text="USER DASHBOARD",font=("Arial Black","20"),fg="black",bg='#8AAAE5',width=50)
User_Dasboard.place(x=290,y=60)

def borrowfunc():
    lb.destroy() 
    import a9_User_borrow_book
Borrow_Book_Button = Button(text="    Borrow Book    ",bg="white",font="50",command=borrowfunc)
Borrow_Book_Button.place(x=60,y=140)

def payfinefunc():
    lb.destroy()
    import a10_user_Payfine

payment_Button = Button(text="       Payment       ",bg="white",font="50",command=payfinefunc)
payment_Button.place(x=60,y=200)


def exitfunc():
    lb.destroy() 
    import a3_login
exit_but = Button(text="  Exit ",bg="white",font="50",command=exitfunc)
exit_but.place(x=1400,y=100)

frame1 = Frame(lb,bg="#7fa5e8",height=220,width=1600)
frame1.place(x=0,y=520)    #used for creating a frame where enquires information will be placed

Enquiry_ = Label(text="Enquries:",font=("Arial","15"),bg="#7fa5e8")
Enquiry_.place(x=15,y=523)  #creating a label Enquriy at the end

Email_id = Label(text="Email:bookwarica7@gmail.com",font=("Arial","15"),bg="#7fa5e8")
Email_id.place(x=15,y=580)
Contact = Label(text="Contact:+977 9742869215",font=("Arial","15"),bg="#7fa5e8")
Contact.place(x=15,y=610)

lb.state('zoomed')
mainloop()

