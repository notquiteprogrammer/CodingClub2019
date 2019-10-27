import csv
import FundInterface
import FundCalculator
from datetime import datetime


# main class
class FundDemo:
    def __init__(self):
        self.variable = 0
        self.create_interface()


    # calls to FundInterface to initialize GUI
    def create_interface(self):
        print("Interface Starting")
        FundInterface.initialize_interface()


# Starts the Program if this file is named "main.py"
if __name__ == "__main__":
    Demo = FundDemo()

else:
    print("Wrong file")
