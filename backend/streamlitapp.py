import os
import streamlit as st

def get_folders_and_files(folder_path='..'):
    """Return a dictionary of folders and their files."""
    folder_dict = {}
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            folder_dict[item] = os.listdir(item_path)
    return folder_dict

def nested_dropdown():
    # Get the folder structure
    folder_structure = get_folders_and_files()

    # Create the first dropdown for folders
    selected_folder = st.selectbox('Select a folder', list(folder_structure.keys()))
    
    # Create a second dropdown for files within the selected folder
    if selected_folder:
        files_in_folder = folder_structure[selected_folder]
        selected_file = st.selectbox('Select a file', files_in_folder)
    
        if selected_file:
            st.write(f'You selected: {selected_folder}/{selected_file}')

# Call the nested dropdown function
nested_dropdown()
