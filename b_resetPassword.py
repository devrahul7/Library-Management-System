from tkinter import *
lb = Tk()
lb.state("zoomed")
lb.title('Library Management System')
lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100")

colour1 = Label(text="      Library Management System                                                                                                                                                                                   Reset Password",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)
colour2.pack(side=BOTTOM)

reset_password = Label(lb,text="Reset Your Password?",font=("Arial Black","40"),fg="blue",bg='#8AAAE5',width=50)
reset_password.pack(padx=20,pady=95)

new_password = Label(lb,text="Type New Password",font=("Arial","20"),bg='#8AAAE5')
new_password.place(x=500,y=300)
new_password_Entry = Entry(lb,font=("Arial","20"),fg= "black",width=17)
new_password_Entry.place(x=800,y=300)
lb.config(bg="#8AAAE5")


retype_password = Label(lb,text="Retype password",bg='#8AAAE5',font=("Arial","20"))
retype_password.place(x=505,y=370)
retype_Entry = Entry(lb,font=("Arial","20"),width=17)
retype_Entry.place(x=800,y=370)

def confirm_but():
    import a_login
confirm_button = Button(lb,text="Confirm",fg="green",bg="white",font=("Arial","15"),width=8,command=confirm_but).place(x=950,y=500)

def exit_but():
    import a_login
Exit_button = Button(lb,text="Exit",fg="red",bg="white",font=("Arial","15"),width=8,command=exit_but).place(x=500,y=500)



mainloop()