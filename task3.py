import os
import shutil
import pandas as pd

# Auto-detect user's Downloads & Temp folders
DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")
TEMP_FOLDERS = [
    os.path.join(os.path.expanduser("~"), "AppData", "Local", "Temp"),  # Windows
    "/tmp"  
]

# File categories for organizing
FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"]
}

#Organizes files in the Downloads folder based on their type.
def organize_files():
    if not os.path.exists(DOWNLOADS_FOLDER):
        print("Downloads folder not found!")
        return

    for file in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, file)
        if os.path.isfile(file_path):
            for folder, extensions in FILE_TYPES.items():
                if file.endswith(tuple(extensions)):
                    folder_path = os.path.join(DOWNLOADS_FOLDER, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, folder_path)

    print("Files have been organized successfully!")
#Cleans a CSV file by removing duplicates and filling missing values.
def clean_data():
    
    file_path = input("Enter the full path of the CSV file to clean: ").strip()

    if not os.path.exists(file_path):
        print("File not found! Please enter a valid path.")
        return

    try:
        df = pd.read_csv(file_path)
        df.drop_duplicates(inplace=True)
        df.fillna("N/A", inplace=True)

        output_path = os.path.join(os.path.dirname(file_path), "cleaned_data.csv")
        df.to_csv(output_path, index=False)

        print(f" Data cleaned successfully! File saved as {output_path}")
    except Exception as e:
        print(f"Error processing CSV file: {e}")

#Clears system temporary files to free up space.
def clear_temp():
    for folder in TEMP_FOLDERS:
        if os.path.exists(folder):
            for file in os.listdir(folder):
                file_path = os.path.join(folder, file)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except PermissionError:
                    pass  

    print("Temporary files have been cleared!")

def main():
    while True:
        print("\n Python Task Automation ")
        print("1. Organize files in Downloads folder")
        print("2. Clean a CSV data file")
        print("3. Clear temporary files")
        print("4. Exit")

        ch = input("\nEnter your choice: ").strip()

        if ch == "1":
            organize_files()
        elif ch == "2":
            clean_data()
        elif ch == "3":
            clear_temp()
        elif ch == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
