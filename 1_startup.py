from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
lb =Tk()  #creating a blank window
lb.title(" Library Management System ") #PROVIDING A TIITLE
lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") #here +100 or - 100 is used to replace window position
lb.config(bg="#8AAAE5")  #DEFINING BG COLOUR OF THE WINDOW
lb.state("zoomed")
 
colour1 = Label(text="    Library Management System ",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)   #used for providing the colouring to the top and bottom side
colour2.pack(side=BOTTOM)

library_photo  = Image.open("y.png")
c=library_photo.resize((190,130))
r = ImageTk.PhotoImage(c)                #IMPORTING IMAGE
image1=Label(image=r,bg="#8AAAE5").pack()

btn_Sign_up = Button(text="Sign in",font=("Arial","15"),bg="#6D7ACF")
btn_Sign_up.place(x=1520,y=80,anchor="e")


library_photo2  = Image.open("x.png")
d=library_photo2.resize((1300,130))
s = ImageTk.PhotoImage(d)                #IMPORTING IMAGE
image2=Label(image=s,bg="#8AAAE5").place(x=500,y=100)


# # intro_text = """A library is a collection of sources of information and similar resources, made accessible 
# # to a defined community for reference or borrowing. It provides physical or digital access 
# # to material and may be a physical building or room, or a virtual space, or both. A library's 
# # collection can include books, periodicals, newspapers, manuscripts, films, maps, prints, 
# # documents, microform, CDs, cassettes, videotapes, DVDs, Blu-ray Discs, e-books, 
# # audiobooks, databases, and other formats. Libraries range in size from a few shelves of 
# # books to several million items. Sidney Sheldon perfectly describes: "Libraries store the 
# # energy that fuels the imagination. They open up windows to the world and inspire us to 
# # explore and achieve, and contribute to improving our quality of life." """


mainloop()