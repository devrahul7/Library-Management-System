from tkinter import *
from tkinter import messagebox
lb = Tk()

lb.geometry("700x700")
lb.title(" Library Management System ") #PROVIDING A TIITLE
lb.config(bg="#8AAAE5") 
lb.iconbitmap("l.ico")


colour1 = Label(text="      Library Management System                                                                           DASHBOARD",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)   #used for providing the colouring to the top and bottom side
colour2.pack(side=BOTTOM)


Add_Book_Button = Button(text="     Add Book     ",bg="white",font="50")
Add_Book_Button.place(x=5,y=120)
Issue_Book_Button = Button(text="    Issue Book    ",bg="white",font="50")
Issue_Book_Button.place(x=5,y=170)
Returned_Book_Button = Button(text="  Returned Book ",bg="white",font="50")
Returned_Book_Button.place(x=5,y=220)
New_Arrivals_Button = Button(text="   NewArrivals    ",bg="white",font="50")   #Buttons 
New_Arrivals_Button.place(x=5,y=270)
See_Suggestions_Button = Button(text="See Suggestions",bg="white",font="50")
See_Suggestions_Button.place(x=5,y=320)
Add_Member_Button = Button(text="  Add Member   ",bg="white",font="50")
Add_Member_Button.place(x=5,y=370)
Pay_Fine_Button = Button(text="      Pay Fine     ",bg="white",font="50")
Pay_Fine_Button.place(x=5,y=420)

frame2= Frame(lb,bg="white",height=50,width=1600)
frame2.place(x=0,y=50)  #this is the upermost white frame where member info ,books , records button are placed

memberinfo_button = Button(text="Members Info",bg="white",font="(Helvetica,60)")
memberinfo_button.place(x=400,y=60)   # creating buttons 

Book_button = Button(text="Books",bg="white",font="(Helvetica,60)")
Book_button.place(x=600,y=60)

Record_button = Button(text="Records",bg="white",font="(Helvetica,60)")
Record_button.place(x=740,y=60)

About_button = Button(text="About",bg="white",font="(Helvetica,60)")
About_button.place(x=900,y=60)
Help_button = Button(text="Help",bg="white",font="(Helvetica,60)")
Help_button.place(x=1020,y=60)


frame1 = Frame(lb,bg="#7fa5e8",height=220,width=1600)
frame1.place(x=0,y=520)    #used for creating a frame where enquires information will be placed

Enquiry_ = Label(text="Enquries:",font=("Arial","15"),bg="#7fa5e8")
Enquiry_.place(x=15,y=523)  #creating a label Enquriy at the end

Email_id = Label(text="Email:rahulraazrs123@gmail.com",font=("Arial","15"),bg="#7fa5e8")
Email_id.place(x=15,y=580)
Contact = Label(text="Contact:+977 9742869215",font=("Arial","15"),bg="#7fa5e8")
Contact.place(x=15,y=610)



def show_message_View_Book():
    messagebox.showinfo("Library Management System", "Click Ok To view")


View_Returned_Book = Button(text='View Returned Book',bg="#8AAAE5",fg="red",font="30",command=show_message_View_Book).place(x=640,y=470)
lb.state('zoomed')  #zoomed full screen
mainloop()