import tkinter as tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox
from db_access.services import userAuthentication

LARGE_FONT = ("Verdana", 12)
BRANCO = "#fff"

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg=BRANCO)

        self.label = Label(self, text="Log in", font=LARGE_FONT, bg=BRANCO, relief="groove")
        self.nomel = Label(self, text="E-mail:", font="Verdana 10", bg=BRANCO, relief="groove")
        self.senhal = Label(self, text="Password:", font="Verdana 10", bg=BRANCO, relief="groove")

        self.nome = Entry(self)
        self.senha = Entry(self, show="*")

        self.label.place(relx=0.5, rely=0.2, anchor='center')
        self.nomel.place(relx=0.4, rely=0.3, anchor='center')
        self.senhal.place(relx=0.4, rely=0.35, anchor='center')
        self.nome.place(relx=0.5, rely=0.3, anchor='center')
        self.senha.place(relx=0.5, rely=0.35, anchor='center')

        self.grid_columnconfigure(3, weight=1)

        self.button = Button(self, text="Log in",
                             command=self.userAuthentication)
        self.button.place(relx=0.5, rely=0.4, anchor='center')

    def userAuthentication(self, *args):
        mail = self.nome.get()
        password = self.senha.get()
        correct_info = userAuthentication(mail, password)

        if (correct_info):
            self.nome.delete(0, 'end')
            self.senha.delete(0, 'end')
            self.controller.show_frame("HomePage")

        else:
            messagebox.showinfo("Failed to login", "E-mail or password is invalid")
            self.controller.show_frame("LoginPage")
            self.nome.delete(0, 'end')
            self.senha.delete(0, 'end')

