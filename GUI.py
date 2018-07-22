error = 0
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import time
from pathlib import Path
from threading import Thread

def workingOnLogin():
    Obj = Automation_NU.automation.loadData_file()
    print(Obj.password)
    Obj.OpenURL()

try:
    import Automation_NU  
    print('\nBoth the Module was installed')
except ImportError as IE:
    error = 1
finally:
    root = Tk()
    root.minsize(height=400,width=400)
    if(error==1):
        img = ImageTk.PhotoImage(Image.open("Error.png"))
        error_label = Label(root, text="Auto Attendance Nu",image=img)
        error_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        messagebox.showwarning("Modules not Installed","Install modules using commands \n1. pip install pyautogui\n2. pip install selenium")
        sys.exit(0)
    else:
        # email_label = Label(root, text="pyautogui")
        # email_label.grid(row=1, column=1)
        if(Automation_NU.automation.is_connected()):
            my_file = Path("user_data.pkl")
            if(my_file.is_file()):
                img = ImageTk.PhotoImage(Image.open("bot.png"))
                error_label = Label(root, text="Auto Attendance Nu",image=img)
                error_label.place(relx=0.5, rely=0.5, anchor=CENTER)
                
                time.sleep(1)
                work_thread = Thread(target=workingOnLogin)
                work_thread.start()
            else:
                img = ImageTk.PhotoImage(Image.open("Error.png"))
                error_label = Label(root, text="Auto Attendance Nu",image=img)
                error_label.place(relx=0.5, rely=0.5, anchor=CENTER)
                messagebox.showwarning("Error 404","Unable to Find the User_data.pkl.\n\nPlease run addData.py to create user_data file")
                sys.exit(1)
        else:
            img = ImageTk.PhotoImage(Image.open("Error.png"))
            error_label = Label(root, text="Auto Attendance Nu",image=img)
            error_label.place(relx=0.5, rely=0.5, anchor=CENTER)
            messagebox.showwarning("Internet Connection","Unable to connect to the Internet")
            sys.exit(1)
           



    root.title("NU-Attendane System")  # Title of the window
    root.mainloop()  # Base Window close

  