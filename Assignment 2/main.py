import os
import zipfile

def zip_folder(folder_path):
    
    if not os.path.isdir(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return
    
    zip_filename = os.path.basename(folder_path) + ".zip"
    zip_file_path = os.path.join(os.path.dirname(folder_path), zip_filename)

    try:
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))
        print(f"Folder '{folder_path}' has been zipped into '{zip_file_path}'")
    except Exception as e:
        print(f"Error: Failed to zip the folder due to {str(e)}")

folder_path = input("Please enter the path to the folder you want to zip: ")
zip_folder(folder_path)
