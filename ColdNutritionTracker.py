import tkinter as tk
from tkinter import messagebox
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
HEIGHT = 700
WIDTH = 800

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sh = client.open("Diet and Trainings")
sheet1 = sh.worksheet("Food 2020")
dataSheet = sh.worksheet("Data")


def search_function(date, product, weight):
    try:
        integer_result = int(weight)
    except ValueError:
        messagebox.showinfo("Error", "weight is not integer")
        return
    try:
        cell = sheet1.find(date)
    except gspread.exceptions.CellNotFound:
        messagebox.showinfo("Error", "There is now such date")
        return
    try:
        productcell = dataSheet.find(product)
    except gspread.exceptions.CellNotFound:
        messagebox.showinfo("Error", "There is now such product")
        return
    cell = sheet1.find(date)
    icell = cell.row
    jcell = cell.col
    kcell = icell+1
    while not sheet1.cell(kcell, jcell).value == '':
        kcell += 1
    sheet1.update_cell(kcell, jcell, product)
    productcell = dataSheet.find(product)
    ipcell = productcell.row
    jpcell = productcell.col
    dataSheet.update_cell(ipcell, jpcell+1, weight)
    for r in range(1, 5):
        sheet1.update_cell(kcell, jcell+r, dataSheet.cell(ipcell, jpcell+r+1).value)


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

button = tk.Button(frame, text="Calculate and add", bg='gray', command=lambda: search_function(entry.get(), entry2.get(), entry3.get()))
button.place(relx=0.1, rely=0.4)

label = tk.Label(frame, text="Date", bg='#eba434')
label.place(relx=0.1, rely=0.1, relwidth=0.1)

entry = tk.Entry(frame, bg='white')
entry.place(relx=0.2, rely=0.1)

label2 = tk.Label(frame, text="Product", bg='#eba434')
label2.place(relx=0.1, rely=0.2, relwidth=0.1)

entry2 = tk.Entry(frame, bg='white')
entry2.place(relx=0.2, rely=0.2)

label = tk.Label(frame, text="Weight", bg='#eba434')
label.place(relx=0.1, rely=0.3, relwidth=0.1)

entry3 = tk.Entry(frame, bg='white')
entry3.place(relx=0.2, rely=0.3)

root.mainloop()

