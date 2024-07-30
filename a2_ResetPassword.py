from tkinter import *
from tkinter import messagebox
lb = Tk()
lb.state("zoomed")
lb.title('Library Management System')
lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100")
lb.config(bg="#8AAAE5")

colour1 = Label(text="      Library Management System \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  Reset Password",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)
colour2.pack(side=BOTTOM)

Label_reset_password = Label(lb,text="Reset Your Password?",font=("Arial Black","25"),fg="blue",bg='#8AAAE5',width=50)
Label_reset_password.pack(padx=20,pady=30)


label_username = Label(lb,text="Username",font=("Arial","20"),bg='#8AAAE5')
label_username.place(x=150,y=170)
username_Entry = Entry(lb,font=("Arial","20"),fg= "black",width=17)
username_Entry.place(x=400,y=170)

old_password = Label(lb,text="      Old Password",font=("Arial","20"),bg='#8AAAE5')
old_password.place(x=80,y=230)
old_password_Entry = Entry(lb,font=("Arial","20"),fg= "black",width=17)
old_password_Entry.place(x=400,y=230)

type_new_password = Label(lb,text="Type New Password",font=("Arial","20"),bg='#8AAAE5')
type_new_password.place(x=80,y=290)
type_new_password_Entry = Entry(lb,font=("Arial","20"),fg= "black",width=17)
type_new_password_Entry.place(x=400,y=290)

retype_password = Label(lb,text="  Retype password",bg='#8AAAE5',font=("Arial","20"))
retype_password.place(x=80,y=350)
retype_Entry = Entry(lb,font=("Arial","20"),width=17)
retype_Entry.place(x=400,y=350)

def Confirm_fun():
    messagebox.showinfo("Library Management System", "Password Reset Succesfully")
    lb.destroy()  # Close the current windows
    import a3_login
  
confirm_button = Button(lb,text="Confirm",fg="green",bg="white",font=("Arial","15"),width=8,command=Confirm_fun).place(x=500,y=600)

def exit_but():
    messagebox.showinfo("Library Management System", "Exited")
    lb.destroy()  # Close the current window
    import a0startup_Page
   
Exit_button = Button(lb,text="Exit",fg="red",bg="white",font=("Arial","15"),width=8,command=exit_but).place(x=950,y=600)

mainloop()




