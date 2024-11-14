import os

def rename_files_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return
    
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    files.sort()
    
    if not files:
        print("The folder is empty. No files to rename.")
        return

    for index, file_name in enumerate(files, start=1):
        file_path = os.path.join(folder_path, file_name)
        file_extension = os.path.splitext(file_name)[1]
        new_file_name = f"{index}{file_extension}"
        new_file_path = os.path.join(folder_path, new_file_name)
        
        try:
            os.rename(file_path, new_file_path)
            print(f"File '{file_name}' renamed to '{new_file_name}'")
        except PermissionError:
            print(f"Error: Unable to rename file '{file_name}' due to permission issues.")
        except Exception as e:
            print(f"Error: Could not rename '{file_name}' due to {str(e)}")

    print("Renaming completed.")

folder_path = input("Please enter the path to the folder: ")
rename_files_in_folder(folder_path)
