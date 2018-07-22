import tkinter
from tkinter import *
from tkinter import messagebox
import pickle
from Automation_NU import *
import socket



def GetDate():
    # print(date.get())
    # print(Month.get())
    # print(user_id.get())
    # print(Password.get())
    # print(year.get()) 
    # print(sem.get())
    au = automation()
    au.loadData(user_id.get(),Password.get(),evenOrodd.get(),sem.get(),year.get())
    messagebox.showwarning("User Data Saved","User Data Saved Successfully. \n \n Now run GUI.py to run the whole program.")
    sys.exit(0)

def semester(self):
    global sem
    if(evenOrodd.get()=="Even Semester"):
        option_sem = OptionMenu(root, sem,"Semester II","Semester IV","Semester VI")
        if(set_var==0):
            pass
        else:
            option_sem.grid_forget()

        option_sem.grid(row=8,column=2)
    else:
        option_sem = OptionMenu(root, sem,"Semester I","Semester III","Semester V","Semester VII")
        if(set_var==0):
            pass
        else:
            option_sem.grid_forget()

        option_sem.grid(row=8,column=2)

root = Tk()
set_var=0
sem = StringVar()
sem.set("")
root.title("Add User Data")
NU_label = Label(root, text="Nucleus Login Details",font=("Helvetica", 16),fg="RED")
NU_label.grid(row=1, column=1,columnspan=2)
username_label = Label(root, text="Username")
username_label.grid(row=2, column=1)
password_label = Label(root, text="Password")
password_label.grid(row=3, column=1)

user_id = StringVar()  # to get the value of Email ID

txt_username = Entry(root, text="Enter UserName", textvariable=user_id)
txt_username.grid(row=2, column=2)

Password = StringVar()  # to get the value of Email ID

txt_pass = Entry(root, text="Enter Password", textvariable=Password,show="*")
txt_pass.grid(row=3, column=2)

NU_label = Label(root, text="Attendance Details",font=("Helvetica", 16),fg="RED")
NU_label.grid(row=4, column=1,columnspan=2)

evenOrodd_label = Label(root,text="select Date")
evenOrodd_label.grid(row=5,column=1)

evenOrodd = StringVar()
evenOrodd.set("Even Semester")

option = OptionMenu(root, evenOrodd, "Even Semester","Odd Semester",command=semester)
option.grid(row=5,column=2)


year_label = Label(root,text="select Year")
year_label.grid(row=7,column=1)

year = StringVar()
year.set("2018-2019")

option_sem = OptionMenu(root,year,"2015-2016","2016-2017","2017-2018","2018-2019","2019-2020","2020-2021","2021-2022")
option_sem.grid(row=7,column=2)

sem_label = Label(root,text="Select Semester")
sem_label.grid(row=8,column=1)


btn_login = Button(root, text="Save User Details",command=GetDate, width = 30 ,fg="blue",font=("Helvetica", 16),bg="#bcc8db")
btn_login.grid(row=9, column=1,columnspan=3)
root.mainloop()