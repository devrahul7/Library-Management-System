from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
lb =Tk()  #creating a blank window
lb.title(" Library Management System ") #PROVIDING A TIITLE
lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") #here +100 or - 100 is used to replace window position
lb.config(bg="#8AAAE5")  #DEFINING BG COLOUR OF THE WINDOW
lb.state("zoomed")
 
colour1 = Label(text="    Library Management System                                                           Welcome to BookWarica Library",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)   #used for providing the colouring to the top and bottom side
colour2.pack(side=BOTTOM)

library_photo  = Image.open("y.png")
c=library_photo.resize((300,250))
r = ImageTk.PhotoImage(c)                #IMPORTING IMAGE
image1=Label(image=r,bg="#8AAAE5").pack()


name1 = Label(text="Library",font=("Arial Bold","20"),fg="#34A853",bg="#8AAAE5")
name1.place(x=600,y=200)

name2 = Label(text="Management",font=("Arial Bold","20"),fg="#FF7A00",bg="#8AAAE5")
name2.place(x=705,y=200)

name3 = Label(text="System",font=("Arial Bold","20"),fg="#34A853",bg="#8AAAE5")
name3.place(x=880,y=200)

label1 = Label(bg="#4285F4",height=3,width=100)
label1.place(x=440,y=245)

yet_name = Label(text="Dont have a account yet?",font=("Arial Bold","15"),fg="black",bg="#4285F4")
yet_name.place(x=450,y=258)

sign_up_button = Button(text="Sign up",font=("Arial Bold","10"),fg="black",bg="#4285F4")
sign_up_button.place(x=1050,y=258)
introduction_label = Label(text="Introduction",font=("Arial Bold","20"),fg="#CC0000",bg="#8AAAE5")
introduction_label.place(x=700,y=320)


intRo_text =  Label(text="Libraries store the energy that fuels the imagination \n        They open up windows to the world and inspire us to explore and achieve,\n and contribute to improving our quality of life.",font=("Arial","15"),fg="black",bg="#8AAAE5")
intRo_text.place(x=440,y=360)

intRo_text2 =  Label(text="Nothing is pleasanter than exploring a library \n So for exploring more click Sign up/Sign in ",font=("Arial","15"),fg="black",bg="#8AAAE5")
intRo_text2.place(x=600,y=450)


btn_Sign_up = Button(text="Sign in",font=("Arial","15"),bg="#6D7ACF")
btn_Sign_up.place(x=1520,y=80,anchor="e")

Bottom_text = Label(text="BookWarica  LiBrarY",font=("Arial Bold","15"),fg="black",bg="#6D7ACF")
Bottom_text.place(x=680,y=750)

mainloop()
