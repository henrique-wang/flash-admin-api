import tkinter as tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox

LARGE_FONT = ("Verdana", 12)
BRANCO = "#fff"

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg=BRANCO)

        self.label = Label(self, text="Please select an action", font=LARGE_FONT, bg=BRANCO, relief="groove")
        self.label.place(relx=0.5, rely=0.2, anchor='center')

        self.addButton = Button(self, text="Add new product",
                             command=lambda: controller.show_frame("AddPage"))
        self.addButton.place(relx=0.5, rely=0.4, anchor='center')

        self.updateButton = Button(self, text="Update a product",
                                command=lambda: controller.show_frame("UpdatePage"))
        self.updateButton.place(relx=0.5, rely=0.45, anchor='center')

        self.logoutButton = Button(self, text="Logout",
                                command=lambda: controller.show_frame("LoginPage"), bg = 'red')
        self.logoutButton.place(relx=0.5, rely=0.5, anchor='center')