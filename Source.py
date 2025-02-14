import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from tkinter import ttk  # Import ttk for Notebook
import pandas as pd
import os
from openpyxl import load_workbook

# Sample Personnel Data
personnel_list = []

# Function to save personnel data to an Excel file
def save_to_excel():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        df = pd.DataFrame(personnel_list)
        df.to_excel(file_path, index=False, engine='openpyxl')
        messagebox.showinfo("Save to Excel", "Personnel data saved successfully.")

# Function to load personnel data from Excel
def load_from_excel():
    global personnel_list
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        personnel_list = pd.read_excel(file_path, engine='openpyxl').to_dict(orient='records')
        update_personnel_listbox()
        messagebox.showinfo("Load from Excel", "Personnel data loaded successfully.")
    else:
        messagebox.showwarning("Load from Excel", "No data file selected.")

# Function to update the personnel list display
def update_personnel_listbox():
    listbox.delete(0, tk.END)
    for person in personnel_list:
        listbox.insert(tk.END, f"{person['Name']} | SSN: {person['SSN']}")

# Function to add new personnel
def add_personnel():
    new_person = {
        'Name': name_entry.get(),
        'Birthdate': birthdate_entry.get(),
        'BloodType': bloodtype_entry.get(),
        'Current Residency': residency_entry.get(),
        'SSN': ssn_entry.get(),
        'PHILHEALTHID': philhealth_entry.get(),
        'OCCUPATION': occupation_entry.get(),
        'Birth Place': birthplace_entry.get(),
        'Home Country': country_entry.get(),
    }
    personnel_list.append(new_person)
    update_personnel_listbox()
    messagebox.showinfo("Add Personnel", "Personnel added successfully.")

# Function to delete personnel
def delete_personnel():
    selected_index = listbox.curselection()
    if selected_index:
        selected_person = personnel_list[selected_index[0]]
        confirm = messagebox.askyesno("Delete Personnel", f"Are you sure you want to delete {selected_person['Name']}?")
        if confirm:
            personnel_list.pop(selected_index[0])
            update_personnel_listbox()

# Function to search personnel by Name, SSN, or PHILHEALTHID
def search_personnel():
    search_term = search_entry.get().lower()
    search_type = search_by_var.get()
    
    matched_personnel = [person for person in personnel_list if search_term in str(person.get(search_type, '')).lower()]
    
    search_results.delete(0, tk.END)
    for person in matched_personnel:
        search_results.insert(tk.END, f"{person['Name']} | SSN: {person['SSN']}")
    
    if not matched_personnel:
        messagebox.showwarning("Search Result", "No personnel found.")

# Function to show detailed dossier of selected personnel
def show_dossier(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_person = personnel_list[selected_index[0]]
        
        # Create a new window (Toplevel) to show the details
        dossier_window = tk.Toplevel(root)
        dossier_window.title(f"Detailed Dossier of {selected_person['Name']}")
        
        # Display each detail as a Label
        for field, value in selected_person.items():
            label = tk.Label(dossier_window, text=f"{field}: {value}")
            label.pack(padx=10, pady=5)

# Creating main window
root = tk.Tk()
root.title("Personnel Management System")

# Tab Control (using Notebook widget from ttk)
tab_control = ttk.Notebook(root)

# Tab 1: Personnel List
tab1 = tk.Frame(tab_control)
tab_control.add(tab1, text='Personnel List')

# Personnel Listbox and Scrollbar
listbox = tk.Listbox(tab1, height=20, width=70)
listbox.pack(padx=10, pady=10)

# Bind double-click event to the listbox to show the dossier
listbox.bind("<Double-1>", show_dossier)

# Buttons for saving and loading Excel
save_button = tk.Button(tab1, text="Save to Excel", command=save_to_excel)
save_button.pack(side=tk.LEFT, padx=10, pady=10)
load_button = tk.Button(tab1, text="Load from Excel", command=load_from_excel)
load_button.pack(side=tk.LEFT, padx=10, pady=10)

# Tab 2: Add Personnel
tab2 = tk.Frame(tab_control)
tab_control.add(tab2, text='Add Personnel')

fields = ["Name", "Birthdate", "Blood Type", "Current Residency", "SSN", "PHILHEALTHID", "Occupation", "Birth Place", "Home Country"]
entries = {}

for field in fields:
    label = tk.Label(tab2, text=f"{field}:")
    label.pack()
    entry = tk.Entry(tab2)
    entry.pack()
    entries[field] = entry

name_entry = entries["Name"]
birthdate_entry = entries["Birthdate"]
bloodtype_entry = entries["Blood Type"]
residency_entry = entries["Current Residency"]
ssn_entry = entries["SSN"]
philhealth_entry = entries["PHILHEALTHID"]
occupation_entry = entries["Occupation"]
birthplace_entry = entries["Birth Place"]
country_entry = entries["Home Country"]

add_button = tk.Button(tab2, text="Add Personnel", command=add_personnel)
add_button.pack(padx=10, pady=10)

# Tab 3: Delete Personnel
tab3 = tk.Frame(tab_control)
tab_control.add(tab3, text='Delete Personnel')

delete_button = tk.Button(tab3, text="Delete Selected Personnel", command=delete_personnel)
delete_button.pack(padx=10, pady=10)

# Tab 4: Search Personnel
tab4 = tk.Frame(tab_control)
tab_control.add(tab4, text='Search Personnel')

search_label = tk.Label(tab4, text="Search by Name, SSN, or PHILHEALTHID:")
search_label.pack(padx=10, pady=10)

search_by_var = tk.StringVar(value="Name")
search_by_menu = tk.OptionMenu(tab4, search_by_var, "Name", "SSN", "PHILHEALTHID")
search_by_menu.pack(padx=10, pady=10)

search_entry = tk.Entry(tab4)
search_entry.pack(padx=10, pady=10)

search_button = tk.Button(tab4, text="Search", command=search_personnel)
search_button.pack(padx=10, pady=10)

search_results = tk.Listbox(tab4, height=10, width=70)
search_results.pack(padx=10, pady=10)

# Pack the tab control
tab_control.pack(expand=1, fill="both")

# Run the app
root.mainloop()
