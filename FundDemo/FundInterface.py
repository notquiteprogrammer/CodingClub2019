from tkinter import *


# This class is the child class of Tk()
class FundInterface(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    # This Function creates the Visuals of the Interface
    def create_widgets(self):
        Label(self.master, text="Hello World", fg="blue").grid(row=0, column=0)


# This function is called by main to initialize the GUI
def initialize_interface():
    fund_interface = FundInterface(master=Tk())
    fund_interface.master.title("Fund Raiser Program")
    fund_interface.mainloop()
