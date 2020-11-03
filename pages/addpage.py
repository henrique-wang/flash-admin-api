import tkinter as tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox
from domain.product_class import Product
from decimal import Decimal

LARGE_FONT = ("Verdana", 12)
BRANCO = "#fff"

class AddPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg=BRANCO)

        self.label = Label(self, text="Add new product", font=LARGE_FONT, bg=BRANCO, relief="groove")
        self.namel = Label(self, text="New Product Name:", font="Verdana 10", bg=BRANCO, relief="groove")
        self.pricel = Label(self, text="New Product Price:", font="Verdana 10", bg=BRANCO, relief="groove")

        self.name = Entry(self)
        self.price = Entry(self)

        self.label.place(relx=0.5, rely=0.2, anchor='center')
        self.namel.place(relx=0.4, rely=0.3, anchor='center')
        self.pricel.place(relx=0.4, rely=0.35, anchor='center')

        self.name.place(relx=0.5, rely=0.3, anchor='center')
        self.price.place(relx=0.5, rely=0.35, anchor='center')

        self.grid_columnconfigure(3, weight=1)

        self.backButton = Button(self, text="Back",
                             command=lambda: self.cancel_add(controller))
        self.backButton.place(relx=0.4, rely=0.4, anchor='center')

        self.nextButton = Button(self, text="Next",
                             command=lambda: self.add_product(controller))
        self.nextButton.place(relx=0.6, rely=0.4, anchor='center')

    def cancel_add(self, controller):
        cancel = messagebox.askokcancel(title=None, message="Do you want to leave this page?")
        if cancel == True:
            controller.show_frame("HomePage")
            controller.product = None

    def add_product(self, controller):
        productName = self.name.get()
        try:
            productPrice = float(self.price.get())
            newProduct = Product(productName, productPrice)
            controller.product = newProduct
            print("Added ", newProduct)
            controller.show_frame("RecordPage")
        except:
            messagebox.showinfo("Error","Price needs to be a decimal number")
            self.controller.show_frame("AddPage")
