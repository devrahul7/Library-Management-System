
n = 0
x = ['ab', 'cd'] 
for i in range(len(x)):
    x.append(i)
 
print(x) 



def clearentry(event):
    if password_Entry.get()== 'Enter Password':
        password_Entry.delete(0,END)
password_Entry.insert(0,'Enter Password')
password_Entry.bind('<FocusIn>',clearentry)

