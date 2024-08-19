from tkinter import *
from tkinter import messagebox
lb = Tk()
lb.geometry("700x700")
lb.title(" Library Management System ") #PROVIDING A TIITLE
lb.config(bg="#8AAAE5") 
lb.iconbitmap("l.ico")

colour2 = Label(bg="#6D7ACF",width=240,height=3)   #used for providing the colouring to the top and bottom side
colour2.pack(side=BOTTOM)

Name_label = Label(text="Library Management System",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
Name_label.pack()
Admin_Dasboard = Label(text="ADMIN DASHBOARD",font=("Arial Black","20"),fg="black",bg='#8AAAE5',width=50)
Admin_Dasboard.place(x=280,y=60)

def ok():
    lb.destroy()
    import a5_Admin_add_book
Add_Book_Button = Button(text="    +Add Book    ",bg="white",font="50",command=ok)
Add_Book_Button.place(x=100,y=220)

def ok8():
    lb.destroy()  
    import a6_admin_booklist
BookList_Button = Button(text="     Book List      ",bg="white",font="50",command=ok8)
BookList_Button.place(x=100,y=280)

def ok7():
    lb.destroy()  
    import a7_admin_add_memebers_
Add_Member_Button = Button(text="  +Add Member ",bg="white",font="50",command=ok7)
Add_Member_Button.place(x=100,y=340)

def log_button():
    messagebox.showinfo("Library Management System", "Log Out Succesfully")
    lb.destroy()  
    import a3_login
logout_button = Button(lb,text="Log Out",fg="red",bg="white",font=("Arial","15"),width=8,command=log_button).place(x=1050,y=600)

lb.state('zoomed')  #zoomed full screen
mainloop()


#codde