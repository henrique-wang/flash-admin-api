import tkinter as tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox
from domain.product_class import Product
from db_access.services import editProduct

LARGE_FONT = ("Verdana", 12)
BRANCO = "#fff"

class UpdatePage2(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg=BRANCO)

        self.label = Label(self, text="Update product", font=LARGE_FONT, bg=BRANCO, relief="groove")
        self.namel = Label(self, text="Product Name:", font="Verdana 10", bg=BRANCO, relief="groove")
        self.pricel = Label(self, text="Product Price:", font="Verdana 10", bg=BRANCO, relief="groove")

        self.name = Entry(self)
        self.name.insert(0, controller.product.getName())
        self.price = Entry(self)
        self.price.insert(0, controller.product.getPrice())

        self.label.place(relx=0.5, rely=0.2, anchor='center')
        self.namel.place(relx=0.4, rely=0.3, anchor='center')
        self.pricel.place(relx=0.4, rely=0.35, anchor='center')

        self.name.place(relx=0.5, rely=0.3, anchor='center')
        self.price.place(relx=0.5, rely=0.35, anchor='center')

        self.grid_columnconfigure(3, weight=1)

        self.backButton = Button(self, text="Back",
                             command=lambda: self.cancel_edit(controller))
        self.backButton.place(relx=0.4, rely=0.4, anchor='center')

        self.nextButton = Button(self, text="Next",
                             command=lambda: self.edit_product(controller))
        self.nextButton.place(relx=0.6, rely=0.4, anchor='center')

    def cancel_edit(self, controller):
        cancel = messagebox.askokcancel(title=None, message='Are you sure you want to exit the application?')
        if cancel == True:
            controller.show_frame("HomePage")
            controller.product = None

    def edit_product(self, controller):
        productName = self.name.get()
        try:
            productPrice = float(self.price.get())
            newProduct = Product(productName, productPrice)
            oldProduct = controller.product
            controller.product = newProduct
            print("Edit:", newProduct)
            msgBox = tk.messagebox.askquestion ('Add photos to database','Do you want to add new photos to database?',icon = 'warning')
            if msgBox == 'yes':
                controller.show_frame("RecordPage")
            else:
                editProduct(oldProduct, newProduct)
                controller.show_frame("HomePage")


        except:
            messagebox.showinfo("Error","Price needs to be a decimal number")
            self.controller.show_frame("UpdatePage2")