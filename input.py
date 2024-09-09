from openpyxl import load_workbook
import pandas as pd
from entry import LocationEntry as LE
import streamlit as st

def display_workbook(file_path):
    # Load the workbook
    book = load_workbook(file_path)
    sheet = book.active

    # Get data from columns A, B, and C
    column_a = sheet['A']
    column_b = sheet['B']
    column_c = sheet['C']

    A = [cell.value for cell in column_a]
    B = [cell.value for cell in column_b]
    C = [cell for cell in column_c]

    # Perform distance calculations (ensure LE is imported correctly)
    for i in range(1, len(A)):  # Start from 1 to skip the header row
        if A[i] and B[i]:  # Ensure origin and destination values are not empty
            C[i].value = LE(A[i], B[i]).get_distance()

    # Save the workbook to a new file to avoid overwriting the temp file
    save_path = file_path.replace(".xlsx", "_updated.xlsx")
    book.save(save_path)

    # Display the updated data using pandas for feedback
    st.dataframe(pd.read_excel(save_path))

    return save_path
