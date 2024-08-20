from tkinter import *
from tkinter import messagebox
lb =Tk()  
lb.title("Library Management System") #PROVIDING A TIITLE

lb.iconbitmap("l.ico")
lb.geometry("700x700+100-100") #here +100 or - 100 is used to replace window position
lb.config(bg="#8AAAE5")  #DEFINING BG COLOUR OF THE WINDOW
lb.state("zoomed")

colour1 = Label(text="    Library Management System                                                                                                                                                                                                 Book list ",font="(Helvetica,60)",anchor="w",bg="#6D7ACF",width=240,height=2)
colour1.pack()

colour2 = Label(bg="#6D7ACF",width=240,height=3)
colour2.pack(side=BOTTOM)


body_books_label = Label(text="Book List", bg="#8AAAE5" ,font=("Arial", 20))
body_books_label.pack(pady=10)

Search_button = Button(text=" Search ",font=("Arial", 15))
Search_button.pack(anchor="w",padx=320,pady=0)

book_number_label = Label(text="Book Number",bg="#8AAAE5" ,font=("Arial", 20))
book_number_label.pack(anchor="w",padx=10)

book_number_entry = Entry( font=("Arial", 20))
book_number_entry.place(x=210,y=150)

def exit_program():
    messagebox.showinfo("Library Management System", "Exited")
    lb.destroy()
    import a4_Admin_Dashboard
# Add Exit button 
exit_button = Button(text="  Exit  ",bg="white" ,font=("Arial", 15), command=exit_program)
exit_button.place(x=1400,y=100)





mainloop()