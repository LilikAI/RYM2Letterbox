import tkinter as tk
from tkinter import filedialog
import csv

class csvEditor:
    def __init__(self, input_file):
        self.input_file = input_file

    def editProcess(self):

        output_file = self.input_file.replace(".csv", "") + "_output.csv"
        headings = ["Title", "Year", "WatchedDate", "Rating10"]

        with open(self.input_file, "r") as in_file, open(output_file, "w", newline = "") as out_file:
            reader = csv.reader(in_file)
            writer = csv.writer(out_file)

            writer.writerow(headings)

            for row in reader:
                year = row[1][:4] #extracts the year from the date assuming a YYYY-MM-DD format
                watched_date = row[2].replace("/", "-")
                writer.writerow([row[0], year, watched_date, row[3]])

class display:
    def popup(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        return file_path
    def editor(self, file_path):
        new_editor = csvEditor(file_path)
        new_editor.editProcess()

new_display = display()
file_path = new_display.popup()
new_display.editor(file_path)