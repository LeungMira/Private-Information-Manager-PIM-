import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd
from openpyxl import load_workbook
from openpyxl.workbook.protection import WorkbookProtection

# List to store personnel data
people = []

# Function to save to Excel with full encryption
def save_to_excel():
    filename = simpledialog.askstring("Save", "Enter filename:")
    if not filename:
        return
    password = simpledialog.askstring("Save", "Enter password:", show='*')
    if not password:
        return
    
    df = pd.DataFrame(people)
    file_path = f"{filename}.xlsx"
    df.to_excel(file_path, index=False)
    
    wb = load_workbook(file_path)
    wb.security = WorkbookProtection(workbookPassword=password, lockStructure=True)
    wb.save(file_path)
    messagebox.showinfo("Success", "Data saved successfully! Keep your password safe.")

# Function to load from Excel
def load_from_excel():
    filename = simpledialog.askstring("Load", "Enter filename:")
    if not filename:
        return
    
    try:
        df = pd.read_excel(f"{filename}.xlsx")
        global people
        people = df.to_dict(orient='records')
        update_listbox()
        messagebox.showinfo("Success", "Data loaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", "Failed to load data! Incorrect password or file corrupted.")
        print(e)

# Function to add a new personnel entry
def add_person():
    person = {field: entries[i].get() for i, field in enumerate(fields)}
    if not person["Name"] or not person["SSN"]:
        messagebox.showerror("Error", "Name and SSN are required!")
        return
    
    people.append(person)
    update_listbox()
    messagebox.showinfo("Success", f"{person['Name']} added successfully!")
    clear_entries()

# Function to delete selected personnel
def delete_person():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "No personnel selected!")
        return
    del people[selected[0]]
    update_listbox()
    messagebox.showinfo("Success", "Personnel deleted successfully!")

# Function to search personnel
def search_person():
    query = entry_search.get().lower()
    listbox.delete(0, tk.END)
    for p in people:
        if query in p["Name"].lower() or query in p["SSN"].lower():
            listbox.insert(tk.END, f"{p['Name']} - SSN: {p['SSN']}")

# Function to display full details of selected personnel
def show_details(event):
    selected = listbox.curselection()
    if not selected:
        return
    person = people[selected[0]]
    details = "\n".join([f"{key}: {value}" for key, value in person.items()])
    messagebox.showinfo("Personnel Details", details)

# Function to update listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for p in people:
        listbox.insert(tk.END, f"{p['Name']} - SSN: {p['SSN']}")

# Function to clear entry fields
def clear_entries():
    for entry in entries:
        entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Personnel Management System")
root.geometry("600x500")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Tab 1: Personnel List
frame_list = ttk.Frame(notebook)
notebook.add(frame_list, text="Personnel List")
listbox = tk.Listbox(frame_list, width=60, height=20)
listbox.pack(pady=10)
listbox.bind("<Double-Button-1>", show_details)
btn_save = tk.Button(frame_list, text="Save to Excel", command=save_to_excel)
btn_save.pack(pady=5)
btn_load = tk.Button(frame_list, text="Load from Excel", command=load_from_excel)
btn_load.pack(pady=5)

# Tab 2: Add Personnel
frame_add = ttk.Frame(notebook)
notebook.add(frame_add, text="Add Personnel")
fields = ["Name", "SSN", "Location", "PhilHealthID", "JobID", "BirthPlacement", "Height", "Weight", "BloodType", "Zipcode", "BirthDate", "Gender"]
entries = []
for i, field in enumerate(fields):
    tk.Label(frame_add, text=field + ":").grid(row=i, column=0, padx=5, pady=2, sticky="w")
    entry = tk.Entry(frame_add)
    entry.grid(row=i, column=1, padx=5, pady=2)
    entries.append(entry)
btn_add = tk.Button(frame_add, text="Add Person", command=add_person)
btn_add.grid(row=len(fields), column=1, pady=10)

# Tab 3: Delete Personnel
frame_delete = ttk.Frame(notebook)
notebook.add(frame_delete, text="Delete Personnel")
btn_delete = tk.Button(frame_delete, text="Delete Selected", command=delete_person)
btn_delete.pack(pady=20)

# Tab 4: Search Personnel
frame_search = ttk.Frame(notebook)
notebook.add(frame_search, text="Search Personnel")
entry_search = tk.Entry(frame_search)
entry_search.pack(pady=5)
btn_search = tk.Button(frame_search, text="Search", command=search_person)
btn_search.pack(pady=5)

root.mainloop()
