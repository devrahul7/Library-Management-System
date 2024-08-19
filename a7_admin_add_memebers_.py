from tkinter import *
from tkinter import messagebox
lb =Tk()  #creating a blank window
lb.title(" Library Management System ") #PROVIDING A TIITLE

lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") #here +100 or - 100 is used to replace window position
lb.config(bg="#8AAAE5")  #DEFINING BG COLOUR OF THE WINDOW
lb.state("zoomed")

colour1 = Label(text="      Library Management System                                                                                                                                                                                       Add Members",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)   #used for providing the colouring to the top and bottom side
colour2.pack(side=BOTTOM)


Add_Book_Text = Label(text="Add Members",font=("Bold Arial","20"),bg="#8AAAE5")
Add_Book_Text.place(x=710,y=55)

Label_Full_Name = Label(text="Full Name",bg="#8AAAE5",font=("Bold Arial","15"))
Label_Full_Name.place(x=250,y=123)
Entry_Label_Full_Name = Entry(lb,width=15,font=('Arial 24'))
Entry_Label_Full_Name.place(x=350,y=112)

Label_Username = Label(text="Username",bg="#8AAAE5",font=("Bold Arial","15"))
Label_Username.place(x=244,y=182)
Label_Username= Entry(lb,width=15,font=('Arial 24'))
Label_Username.place(x=350,y=170)

Label_Email = Label(text="Email",bg="#8AAAE5",font=("Bold Arial","15"))
Label_Email.place(x=280,y=240)

Label_Email_Entry= Entry(lb,width=15,font=('Arial 24'))
Label_Email_Entry.place(x=350,y=230)



Label_Phone_number = Label(text="      Phone Number",bg="#8AAAE5",font=("Bold Arial","15"))
Label_Phone_number.place(x=170,y=300)
Label_Phone_number_Entry = Entry(lb,width=15,font=('Arial 24'))
Label_Phone_number_Entry.place(x=350,y=290)

def add_member_func():
    messagebox.showinfo("Library Management System", "Member Added Succesfully")
    lb.destroy()
    import a9_Admin_Dashboard
Add_member = Button(text="Add Members",font=('Arial'),command=add_member_func)
Add_member.place(x=150,y=600)

def Update_func():
    messagebox.showinfo("Library Management System", "Member Updated Succesfully")
    lb.destroy()
    import a9_Admin_Dashboard
Button_update_member = Button(text="Update  Members",font=('Arial'),command=Update_func)
Button_update_member.place(x=310,y=600)

def Retrieve_fun():
    messagebox.showinfo("Library Management System", "Member Retrieved Succesfully")
    lb.destroy()
    import a9_Admin_Dashboard
Button_Retrieve_member = Button(text="Retrieve Members",font=('Arial'),command=Retrieve_fun)
Button_Retrieve_member.place(x=500,y=600)

def del_func():
    messagebox.showinfo("Library Management System", "Book Delete Succesfully")
    lb.destroy()
    import a9_Admin_Dashboard
Button_Delete_Member = Button(text="Delete Members",font=('Arial'),command=del_func)
Button_Delete_Member.place(x=700,y=600)

def exitfunc():
    messagebox.showinfo("Library Management System", "Exited")
    lb.destroy()
    import a4_Admin_Dashboard
Button_Exit = Button(text="   Exit   ",font=('Arial'),command=exitfunc)
Button_Exit.place(x=1400,y=100)  



mainloop()


 