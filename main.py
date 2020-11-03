import tkinter as tk
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from pages.addpage import AddPage
from pages.updatepage import UpdatePage
from pages.updatepage2 import UpdatePage2
from pages.recordpage import RecordPage

LARGEFONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 20)

recog_result = None

# Select which application mode do you want to use
# TEST mode -> recognizes objects from bananas.jpg
# APPLICATION mode -> recognizes objects from picture taken from webcam
# MODE = "TEST"
MODE = "APPLICATION"

class FlashMallAdmin(tk.Tk):

    # __init__ function for class FlashMallClient
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # Product Variables
        self.product = None

        # creating a container
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.curr_page = LoginPage(self.container, self)

        # to display the current frame passed as
        self.show_frame("LoginPage")

        # MODE
        self.MODE = MODE

    # parameter
    def show_frame(self, page):
        self.curr_page.destroy()
        print(page)
        if (page == "LoginPage"):
            self.curr_page = LoginPage(self.container, self)
        elif (page == "HomePage"):
            self.curr_page = HomePage(self.container, self)
        elif (page == "RecordPage"):
            self.curr_page = RecordPage(self.container, self)
        elif (page == "UpdatePage"):
            self.curr_page = UpdatePage(self.container, self)
        elif (page == "AddPage"):
            self.curr_page = AddPage(self.container, self)
        elif (page == "UpdatePage2"):
            self.curr_page = UpdatePage2(self.container, self)

        self.curr_page.grid(row=0, column=0, sticky="nsew")

def main():
    app = FlashMallAdmin()
    app.mainloop()
main()
