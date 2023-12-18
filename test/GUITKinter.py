# Import the required libraries
import tkinter as tk
from tkinter import ttk

# Create a root window
root = tk.Tk()
root.geometry('600x400')

# Create a Notebook widget
nb = ttk.Notebook(root)

# Create the frames for each tab
tab1 = ttk.Frame(nb)
tab2 = ttk.Frame(nb)

# Add the tabs to the notebook with icons
nb.add(tab1, text='Tab 1', image='icon1.ico', compound=tk.LEFT)
nb.add(tab2, text='Tab 2', image='icon2.ico', compound=tk.LEFT)

# Create the text field for title input
title = tk.StringVar()
title_entry = ttk.Entry(tab1, textvariable=title)
title_entry.insert(0, "Enter title here")
title_entry.pack(fill=tk.BOTH, expand=True)







# Create the table with specified labels
tree = ttk.Treeview(tab1, columns=('lat', 'long', 'name', 'value'), show='headings')
tree.heading('lat', text='lat')
tree.heading('long', text='long')
tree.heading('name', text='name')
tree.heading('value', text='value')
tree.pack(fill=tk.BOTH, expand=True)

tree.insert(parent='', index=0, values=('15', '14', 'test', '50'))







# Define the function for adding a row
def add_row():
    tree.insert('', 'end', values=("0", "0", "name", "value"))

# Define the function for deleting a row
def delete_row():
    selected_items = tree.selection()
    for selected_item in selected_items:
        tree.delete(selected_item)

# Define the function for editing a row
def edit_row(event):
    item = tree.identify('item', event.x, event.y)
    column = tree.identify('column', event.x, event.y)
    value = tree.set(item, column)
    new_value = simpledialog.askstring("Edit", "Enter new value:", initialvalue=value)
    if new_value is not None:
        tree.set(item, column, new_value)

# Bind the double click event to the edit_row function
tree.bind('<Double-1>', edit_row)

# Create the buttons for adding and deleting rows
add_button = ttk.Button(tab1, text="Add Row", command=add_row)
delete_button = ttk.Button(tab1, text="Delete Row", command=delete_row)
add_button.pack(fill=tk.BOTH, expand=True)
delete_button.pack(fill=tk.BOTH, expand=True)

# Pack the notebook
nb.pack(fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
root.mainloop()
