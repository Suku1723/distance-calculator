import customtkinter as ctk
from tkinter import filedialog
import pandas as pd
from entry import LocationEntry

def calculate_distances(addresses, EntryList):
    # Placeholder function to calculate distances between addresses
    # Replace this with your actual distance calculation logic
    distances = []
    for i in range(len(addresses) - 1):
        distance = f"Distance between {addresses[i]} and {addresses[i+1]}: {EntryList[i].get_distance()} mi\n"
        distances.append(distance)
    return distances

def open_file():
    # Open file dialog and get the file path
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)
        EntryList = []

        # Assume addresses are in a column named 'Address'
        if 'Address' in df.columns:
            addresses = df['Address'].tolist()

            # # Calculate distances
            # distances = calculate_distances(addresses)

            # Initialize as LocationEntry Objects
            for i in range(len(addresses)-1):
                EntryList.append(LocationEntry(addresses[i], addresses[i+1]))

            distances = calculate_distances(addresses, EntryList)

            # Clear the text widget
            text_widget.delete('1.0', ctk.END)

            # Insert the distances into the text widget
            for distance in distances:
                text_widget.insert(ctk.END, distance + '\n')
        else:
            text_widget.delete('1.0', ctk.END)
            text_widget.insert(ctk.END, "No 'Address' column found in the Excel file.")

# Create the main window
root = ctk.CTk()
root.title("Excel Address Distance Calculator")

# Create a button to open the file dialog
open_button = ctk.CTkButton(root, text="Open Excel File", command=open_file)
open_button.pack(pady=10)

# Create a text widget to display the distances
text_widget = ctk.CTkTextbox(root, wrap='none', height=400, width=600)
text_widget.pack(pady=10)

# Add scrollbars to the text widget
x_scrollbar = ctk.CTkScrollbar(root, orientation='horizontal', command=text_widget.xview)
x_scrollbar.pack(side=ctk.BOTTOM, fill=ctk.X)
text_widget.configure(xscrollcommand=x_scrollbar.set)

y_scrollbar = ctk.CTkScrollbar(root, orientation='vertical', command=text_widget.yview)
y_scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)
text_widget.configure(yscrollcommand=y_scrollbar.set)

# Run the application
root.mainloop()
