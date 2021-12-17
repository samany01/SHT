from tkinter import *
import keyboard
import math
import time
from tkinter import messagebox
import os
from threading import *


def restart_button():
    os.system("shutdown /r")


class MyWindow:

    def __init__(self, win):
        self.entery1 = Entry(win, highlightthickness=.5, font=("impact", 70), justify='center')
        self.entery1.config(highlightbackground="azure", highlightcolor="lightgrey")
        self.entery1.place(x=410, y=270, width=110, height=90)

        self.entery2 = Entry(win, highlightthickness=.5, font=('impact', 70), justify='center')
        self.entery2.config(highlightbackground="azure", highlightcolor="lightgrey")
        self.entery2.place(x=410, y=390, width=110, height=90)

        self.button1 = Button(win, text="Intialize", bg="skyblue", command=self.threading, font=("Bell MT", 25))
        self.button1.place(x=490, y=545, width=120, height=54)

        self.button2 = Button(win, text="Shutdown", bg="skyblue", command=self.shutdown_button, font=("Bell MT", 25))
        self.button2.place(x=311, y=545, width=164, height=54)

        self.button3 = Button(win, text="Restart", bg="skyblue", command=self.restart_button, font=("Bell MT", 25))
        self.button3.place(x=165, y=545, width=131, height=54)

        self.button4 = Button(win, text="Cancel", bg="skyblue", command=self.cancel_button, font=("Bell MT", 25))
        self.button4.place(x=30, y=545, width=120, height=54)

        win.bind('<Return>', self.threading)

    def restart_button(self):
        os.system("shutdown /r")

    def shutdown_button(self):
        os.system("shutdown /s")

    def cancel_button(self):
        window.quit()

    def count_sec(self, _event=None):
         hours = self.entery1.get()
         minutes = self.entery2.get()

         if hours == "" and minutes != "":
             hours = float(hours + "0")

         if hours != "" and minutes == "":
             minutes = float(minutes + "0")

         if float(hours) == 0 and float(minutes) == 0:
             messagebox.showerror("SHT", "Please enter positive numbers")

         elif float(hours) >= 0 and float(minutes) >= 0:
             hrs_to_sec = float(hours) * 60 * 60
             mins_to_sec = float(minutes) * 60
             print(f'{math.ceil(hrs_to_sec) + math.ceil(mins_to_sec)} sec')
             total = math.ceil(hrs_to_sec) + math.ceil(mins_to_sec)

             for i in range(0, total + 1):
                 i = total - i
                 time.sleep(1)

                 if i == 0:
                     messagebox.showinfo("SHT", "GOOD-BYE")
                     os.system("shutdown /s")


         while float(hours) < 0 or float(minutes) < 0:
              messagebox.showerror("SHT", "Please enter positive numbers")
              break

    def trail(self, _event=None):
        try:
            self.count_sec()
        except ValueError:
            messagebox.showinfo("SHT", "Invailed entery")

    def threading(self, _event=None):
        thread = Thread(target=self.trail)
        thread.daemon = True
        thread.start()

if __name__ == "__main__":


    window = Tk()
    img = PhotoImage(file='Picture1.png')
    Label(window, image=img).pack()
    dd = PhotoImage(file="Picture3.png")
    window.iconphoto(False, dd)
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    width = 640
    height = 620
    left = (screenWidth - width) / 2
    top = (screenHeight - height) / 2
    window.geometry("%dx%d+%d+%d" % (width, height, left, top))
    window.minsize(640, 620)
    window.maxsize(640, 620)
    window.title("Shut_down Timer")

    mywindow = MyWindow(window)
    window.mainloop()
