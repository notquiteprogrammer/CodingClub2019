import csv


class FundCalculator:
    def __init__(self):
        with open("filename.csv", "r") as csv_file:
            self.csv_reader = csv.reader(csv_file, newline="")

    def calculate_total(self, timerange="all"):

        if timerange == "all":
            pass
        elif timerange == "month":
            pass
        elif timerange == "week":
            pass
        elif timerange == "day":
            pass
        elif timerange == "hour":
            pass
        else:
            print("Pick a time range")

    def get_csv_reader(self):
        return self.csv_reader
