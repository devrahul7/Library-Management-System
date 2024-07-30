from tkinter import *

from tkinter import messagebox
lb =Tk()  #creating a blank window
lb.title(" Library Management System ") #PROVIDING A TIITLE

lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") #here +100 or - 100 is used to replace window position
lb.config(bg="#8AAAE5")  #DEFINING BG COLOUR OF THE WINDOW
lb.state("zoomed")
 
colour1 = Label(text="      Library Management System                                                                                                                                                                                       Signup now",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)   #used for providing the colouring to the top and bottom side
colour2.pack(side=BOTTOM)

Sign_Up_page = Label(text="Signup Page",bg="white",font=("Bold Arial","17"),width=13,height=1)   #used for providing the colouring to the top and bottom side
Sign_Up_page.place(x=710,y=70)

Name_Label = Label(text="Name",font=("Bold Arial","20"),bg="#8AAAE5")
Name_Label.place(x=250,y=115)
Entry_Name = Entry(lb,width=15,font=('Arial 20'))
Entry_Name.place(x=350,y=115)

Label_Student_ID = Label(text="Student ID",bg="#8AAAE5",font=("Bold Arial","20"))
Label_Student_ID.place(x=200,y=170)
Entry_Student_ID= Entry(lb,width=15,font=('Arial 20'))
Entry_Student_ID.place(x=350,y=170)


date_of_birth_name = Label(text="Date of Birth",bg="#8AAAE5",font=("Bold Arial","20"))
date_of_birth_name.place(x=180,y=225)
Entry_date_of_birth = Entry(lb,width=15,font=('Arial 20'))
Entry_date_of_birth.place(x=350,y=225)


Contact_name = Label(text="Contact",bg="#8AAAE5",font=("Bold Arial","20"))
Contact_name.place(x=230,y=280)
Entry_contact = Entry(lb,width=15,font=('Arial 20'))
Entry_contact.place(x=350,y=280)

Addres_name = Label(text="Address",bg="#8AAAE5",font=("Bold Arial","20"))
Addres_name.place(x=230,y=335)
Addres_Entry = Entry(lb,width=15,font=('Arial 20'))
Addres_Entry.place(x=350,y=335)


def show_message_box():
    messagebox.showinfo("Library Management System", "Sign up Succesfully")
Sign_up_page_button = Button(text="Signup",font=('Arial'),command=show_message_box)
Sign_up_page_button.place(x=350,y=500)
#problemm in entry box

def show_message_box2():
    messagebox.showinfo("Library Management System", "Exited")
Button_Exit = Button(text="   Exit   ",font=('Arial'),command=show_message_box2)
Button_Exit.place(x=1100,y=500)   




mainloop()