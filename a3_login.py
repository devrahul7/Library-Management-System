from tkinter import *
from PIL import Image,ImageTk
import sqlite3   
lb =Tk()  #creating a blank window
lb.title(" Library Management System ") #PROVIDING A TIITLE
lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") #here +100 or - 100 is used to replace window position
lb.config(bg="#8AAAE5")  #DEFINING BG COLOUR OF THE WINDOW
admin = Label(lb,text="Library Login",font=("Bold Arial","30"),bg="#8AAAE5",fg="#000000")
admin.place(x=900,y=150)

library_photo  = Image.open("zbc.png")
c=library_photo.resize((850,690))
r = ImageTk.PhotoImage(c)                #IMPORTING IMAGEs
image1=Label(image=r).place(x=0,y=50)


colour1 = Label(text="    Library Management System",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=3)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)
colour2.pack(side=BOTTOM)

#BAckend Works
conn=sqlite3.connect('LB.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS login_library(
u TEXT,
p TEXT)''')
conn.commit()
conn.close()

def login_1():
    conn = sqlite3.connect("lb.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO login_library(u,p) VALUES(?,?)",
        (User_Entry.get(), password_Entry.get())
    )
    conn.commit()
    conn.close()
    User_Entry.delete(0, END)
    password_Entry.delete(0, END)
    
username = Label(lb,text="Username",font="34",bg="#8AAAE5")
username.place(x=900,y= 270)
password= Label(lb,text="Password",font="34",bg="#8AAAE5",fg="black")
password.place(x=900,y=360)
log_inButton = Button(lb,text="Login",font= ("4"),fg="black",bg= "white",command=login_1)
log_inButton.place(x=900,y=550,height=35)     #CREATING A LOG IN BUTTON

def onclick(event,text):
    if event.widget.get()==text:
        event.widget.delete(0,END)
        event.widget.insert(0,'')
def offclick(event,text):
    if event.widget.get()=='':
        event.widget.insert(0,text)
def resetfuc():
    lb.destroy()  # Close the current window
    import a2_ResetPassword 

reset_Button = Button(lb,text="Reset Password?",font= ("4"),fg="black",bg= "white",command=resetfuc)
reset_Button.place(x=1060,y=550,height=35)  #CREATING A RESET BUTTON
placeholder='Enter Username or Email'
User_Entry = Entry(lb,font="20",bg='white',fg="black")
User_Entry.place(x=900,y=310,height=35,width=235) #USER ENTRY BOX
User_Entry.insert(0,'Enter Username or Email')
User_Entry.bind('<FocusIn>',lambda event,text=placeholder:onclick(event,text))
User_Entry.bind('<FocusOut>',lambda event,text=placeholder:offclick(event,text))

placeholder1='Enter Password'
password_Entry = Entry(font="25", show="*")  #PASSWORD ENTRY BOX
password_Entry.place(x=900,y=397,height=35,width=235)
password_Entry.insert(0,'Enter Password')
password_Entry.bind('<FocusIn>',lambda event,text=placeholder1:onclick(event,text))
password_Entry.bind('<FocusOut>',lambda event,text=placeholder1:offclick(event,text))

def add():
    if a.get()==0:
        password_Entry.config(show="*")
    else:
        password_Entry.config(show="")

a = IntVar()
Show_Password_Button1 = Checkbutton(text="Show Password",bg="#8AAAE5",variable=a,command=add,font="20")
Show_Password_Button1.place(x=900,y=460)
lb.state('zoomed')

mainloop()

#coddes