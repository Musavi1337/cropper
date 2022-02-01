import cropper as cropp
import tkinter as tk
from tkinter import *
from tkinter import ttk


class mainWindow(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("ALL IN ONE")
        self.cleanUpBtn = Button(
            self,
            text="Click here to clean up file with predetermined values",
            width=40,
            height=5,
            justify="center",
            command=cropp.cleanUp,
        )
        self.cleanUpBtn.grid(
            row=0,
            column=1,
            columnspan=2,
        )
        self.queryCheckBtn = Button(
            self,
            text="Click here to input your own query",
            width=40,
            height=5,
            justify="center",
            command=self.newQueryWindow,
        )
        self.queryCheckBtn.grid(
            row=1,
            column=1,
            columnspan=2,
        )

    def newQueryWindow(self):
        self.newWindow = queryWindow()


class queryWindow(Frame):
    def __init__(self):
        new = tk.Frame.__init__(self)
        new = Toplevel(self)
        new.geometry("250x150")
        new.queryEntry = Entry(new, width=50)
        new.queryEntry.insert(0, "Enter your query here")
        new.queryEntry.pack()
        new.doneButton = Button(
            new,
            text="Click here to crop file",
            width=30,
            height=5,
            justify="center",
            command=lambda: self.queryCheckFun(new.queryEntry.get()),
        )
        new.doneButton.pack()

    def queryCheckFun(self, queryEntry):
        print(queryEntry)
        cropp.queryCheck(queryEntry)
        self.destroy()


def main():
    mainWindow().mainloop()


if __name__ == "__main__":
    main()
