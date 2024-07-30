from tkinter import *
from tkinter import messagebox
lb =Tk()  #creating a blank window
lb.title("Library Management System ") #PROVIDING A TIITLE

lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") #here +100 or - 100 is used to replace window position
lb.config(bg="#8AAAE5")  #DEFINING BG COLOUR OF THE WINDOW
lb.state("zoomed")

colour1 = Label(text="      Library Management System                                                                                                                                                                                    Suggestion Box",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()
colour2 = Label(bg="#6D7ACF",width=240,height=3)   #used for providing the colouring to the top and bottom side
colour2.pack(side=BOTTOM)


Sugestion_Box_Text = Label(text="Suggestion Box",font=("Bold Arial","20"),bg="#8AAAE5")
Sugestion_Box_Text.place(x=710,y=55)







def show_message_box():
    messagebox.showinfo("Library Management System", "Marked Succesfully")
Mark_as_Read = Button(text="Mark as Read",font=('Arial'),command=show_message_box)
Mark_as_Read.place(x=350,y=500)
#problemm in entry box
def show_message_box2():
    messagebox.showinfo("Library Management System", "Exited")
Button_Exit = Button(text="   Exit   ",font=('Arial'),command=show_message_box2)
Button_Exit.place(x=1100,y=500)   



mainloop()