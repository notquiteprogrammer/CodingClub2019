import csv
import FundInterface
import FundCalculator


# main class
class FundDemo:
    def __init__(self):
        self.variable = 0
        with open("accountbook.csv", "w", newline="") as csv_file:
            self.csv_write = csv.writer(csv_file, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        self.create_interface()

    # calls to FundInterface to initialize GUI
    def create_interface(self):
        print("Interface Starting")
        FundInterface.initialize_interface()

    def write_file(self):
        self.csv_write.writerow(["hello", "Test", "ing"])


# Starts the Program if this file is named "main.py"
if __name__ == "__main__":
    Demo = FundDemo()

else:
    print("Wrong file")
