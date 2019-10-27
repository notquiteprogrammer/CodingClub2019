import tkinter as tk
from time import strftime
from csv_file_mod import write_file
from datetime import datetime


# This class is the child class of tk.Frame
# Creates the Interface
class FundInterface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.clock = tk.Label(self.master, font=('8514oem', 20, 'bold'),
                         background='light gray',
                         foreground='black')
        # Item names
        self.item_one = "Coffee"
        self.item_two = "Espresso"
        self.item_three = "Cupcakes"
        self.item_four = "Soft Drinks"
        self.item_five = "Blank"

        # Item prices
        self.item_one_price = 1
        self.item_two_price = 2
        self.item_three_price = 1
        self.item_four_price = 1
        self.item_five_price = 1

        # Food button check
        self.item_one_select = tk.BooleanVar()
        self.item_two_select = tk.BooleanVar()
        self.item_three_select = tk.BooleanVar()
        self.item_four_select = tk.BooleanVar()
        self.item_five_select = tk.BooleanVar()

        # Numeric value check
        self.item_one_value = tk.IntVar()
        self.item_two_value = tk.IntVar()
        self.item_three_value = tk.IntVar()
        self.item_four_value = tk.IntVar()
        self.item_five_value = tk.IntVar()

        # Locations
        self.location = tk.StringVar()
        self.location_list = [(0, "CA"), (1, "CF"), (2, "CT"), (3, "CG")]

        # Images
        # Donut Initialization
        self.img = tk.PhotoImage(file="donut_clipart.png")
        self.canva = tk.Canvas(self.master, width=10, height=10)

        self.create_widgets()
        self.time_clock()

    # This Function creates the Visuals of the Interface
    def create_widgets(self):
        # Title Label
        tk.Label(self.master, text="FundCC", fg="black",
                 font=("8514oem", 40)).grid(row=0, column=0, columnspan=3)

        # Digital Clock grid
        self.clock.grid(row=1, column=0)

        # Item buttons
        item_select_array = [(4, self.item_one_select, self.item_one, self.item_one_value),
                             (5, self.item_two_select, self.item_two, self.item_two_value),
                             (6, self.item_three_select, self.item_three, self.item_three_value),
                             (7, self.item_four_select, self.item_four, self.item_four_value),
                             (8, self.item_five_select, self.item_five, self.item_five_value)]

        for row, item_select, item_name, item_value in item_select_array:
            # Item Boolean Check Button
            tk.Checkbutton(self.master, text=item_name, variable=item_select,
                           font=("8514oem", 15)).grid(row=row, column=0, sticky=tk.W)

            # Item numeric count Radio Buttons
            for i in range(1, 6):
                tk.Radiobutton(self.master, variable=item_value,
                               value=i).grid(row=row, column=i)

        # Numeric Count Labels
        for i in range(1, 6):
            tk.Label(self.master, text=str(i), fg="black",
                     font=("8514oem", 15)).grid(row=1, column=i)

        # Blank Label
        tk.Label(self.master).grid(row=9)

        # Location Label
        tk.Label(self.master, text="Location", fg="black",
                 font=("8514oem", 15)).grid(row=10, sticky=tk.W)

        # Location Radio Buttons
        for i, location in self.location_list:
            tk.Radiobutton(self.master, text=location,
                           variable=self.location,
                           value=location,
                           font=("8514oem", 10)).grid(row=11+i, column=0, sticky=tk.W)
        self.location.set(self.location_list[0][1])

        # Image Canvas
        self.canva.grid(row=10, column=1, columnspan=5, rowspan=5, sticky=tk.NW)
        self.canva.create_image(0, 0, image=self.img)


        # Submit Button which runs the save_inputs function
        tk.Button(self.master, text="Submit", command=self.save_inputs).grid(row=15, column=0, sticky=tk.E)

    def save_inputs(self):
        sales_matrix = \
        [datetime.now(),
         self.location.get(),
         [self.item_one, self.item_one_select.get(), self.item_one_value.get(), self.item_one_price],
         [self.item_two, self.item_two_select.get(), self.item_two_value.get(), self.item_two_price],
         [self.item_three, self.item_three_select.get(), self.item_three_value.get(), self.item_three_price],
         [self.item_four, self.item_four_select.get(), self.item_four_value.get(), self.item_four_price],
         [self.item_five, self.item_five_select.get(), self.item_five_value.get(), self.item_five_price]]

        # Calls to csv_file_mod to write information into "accountbook.csv"
        write_file(sales_matrix)
        print("written to file")
        print(sales_matrix)

        # Resets the interface except Location
        self.reset_interface()

    def reset_interface(self):

        # Resets Food Check Buttons
        self.item_one_select.set(False)
        self.item_two_select.set(False)
        self.item_three_select.set(False)
        self.item_four_select.set(False)
        self.item_five_select.set(False)

        # Resets Food Count Buttons
        self.item_one_value.set(0)
        self.item_two_value.set(0)
        self.item_three_value.set(0)
        self.item_four_value.set(0)
        self.item_five_value.set(0)

    # Recursive Function to create a digital clock
    def time_clock(self):
        string = strftime('%H:%M:%S %p')
        self.clock.config(text=string)
        self.clock.after(1000, self.time_clock)

    def select_food(self):
        # Test Food Check Boolean Values
        print(self.item_one_select.get())
        print(self.item_two_select.get())
        print(self.item_three_select.get())
        print(self.item_four_select.get())
        print(self.item_five_select.get())

        # Test Food Count Values
        print("food 1: " + str(self.item_one_value.get()))
        print("food 2: " + str(self.item_two_value.get()))
        print("food 3: " + str(self.item_three_value.get()))
        print("food 4: " + str(self.item_four_value.get()))
        print("food 5: " + str(self.item_five_value.get()))

    def output_box(self):
        print(self.location.get())


# This function is called by main to initialize the GUI
def initialize_interface():
    fund_interface = FundInterface(master=tk.Tk())
    fund_interface.master.title("FundCC Interface")
    fund_interface.mainloop()
