import streamlit as st
import pandas as pd
import tempfile
from openpyxl import load_workbook
from input import display_workbook

st.title("Excel Distance Calculator App")

# Upload the Excel file
workbook = st.file_uploader('Upload an Excel Workbook', type=["xlsx"])

if workbook is not None:
    # Reading and displaying the uploaded file using pandas
    df = pd.read_excel(workbook)
    st.dataframe(df)

    # Creating an 'Update' button to trigger distance calculations
    update = st.button("Update with Distances")

    if update:
        # Write the uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp_file:
            tmp_file.write(workbook.getbuffer())  # Write the file content correctly
            tmp_file.flush()  # Ensure all content is written to the file
            
            tmp_file_path = tmp_file.name

        # Process the workbook using your custom function
        save_path = display_workbook(tmp_file_path)

        # Open the modified workbook for download
        with open(save_path, "rb") as updated_file:
            st.download_button(
                label="Download Updated File",
                data=updated_file,
                file_name="Updated_Workspace.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                type="primary"
            )