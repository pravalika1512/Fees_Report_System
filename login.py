import tkinter
from tkinter import messagebox
import os

window=tkinter.Tk()
window.title("Login form")
window.geometry('500x500')
window.configure(bg="#333333")

def logi():
    u_name="Admin"
    pass1="admin123"
    if u_entry.get()==u_name and p_entry.get()==pass1:
        
        filename = 'Fee_Frontend.py'
        os.system(filename)
        os.system('notepad'+filename)
    else:
        messagebox.showerror(title="Error",message="Invalid Username or Password")


frame=tkinter.Frame(bg="#333333")

# creating widgets
login_label=tkinter.Label(frame,text="Login",bg='#333333',fg="#FF3399",font=("arial",30))
u_label=tkinter.Label(frame,text="User Name",bg="#333333",fg="#FFFFFF",font=("arial",16))
u_entry=tkinter.Entry(frame,font=("arial",16))
p_entry=tkinter.Entry(frame,show="*",font=("arial",16))
p_label=tkinter.Label(frame,text="Password",bg="#333333",fg="#FFFFFF",font=("arial",16))
login_b=tkinter.Button(frame,text="Login",fg="#FFFFFF",bg="#FF3399",font=("arial",16),command=logi)


# placing widgets on screen
login_label.grid(row=0,column=0,columnspan=2,sticky="news",pady=40)
u_label.grid(row=1,column=0)
u_entry.grid(row=1,column=1,pady=20)
p_entry.grid(row=2,column=1)
p_label.grid(row=2,column=0,pady=20)
login_b.grid(row=3,column=0,columnspan=2,pady=30)

frame.pack()
window.mainloop()

