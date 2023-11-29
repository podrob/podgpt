import shutil
import os

FOLDER = "./docs"

class FileManager:
    def save_files(self, uploaded_files):
        if not os.path.exists(FOLDER):
            os.makedirs(FOLDER)
        
        for file in uploaded_files:
            if file:
                with open(os.path.join(FOLDER, file.name), "wb") as f:
                    f.write(file.read())

    def remove_folder(self, folder):
        try:
            shutil.rmtree(folder)
            print(f"Folder '{folder}' has been successfully deleted.")
        except FileNotFoundError:
            print(f"Folder '{folder}' not found.")
        except PermissionError:
            print(f"You do not have permission to delete '{folder}'.")

    def clear(self):
        self.remove_folder(FOLDER)

    def getFiles():
        # list to store files
        file_names = []

        # Iterate directory
        try: 
            for file_path in os.listdir(FOLDER):
                # check if current file_path is a file
                if os.path.isfile(os.path.join(FOLDER, file_path)):
                    # add filename to list
                    file_names.append(file_path)
            return file_names
        except IOError as e:
                raise Exception("No files exist in the database".format(e.errno, e.strerror))
        