import os
import shutil

def organize_folder():
    base = input("Folder to organize(type the whole path): ")

    if not os.path.exists(base):
        print("Folder not found.")
        return
    print("The way the organizer works is that it puts image files on a specific folder, documents on a specific folder, and so on and so forth. Do you want to proceed?(y/N)")
    choice = input("")
    if choice.lower()  == "y":
     
        folders = {
            "Images": [".jpg", ".png", ".jpeg"],
            "Documents": [".pdf", ".txt", ".docx"],
            "Videos": [".mp4", ".mov"],
            "Music": [".mp3"],
            "Spreadsheets": [".csv", ".xlsx"]
        }
        for folder in folders:
            path = os.path.join(base, folder)
            if not os.path.exists(path):
                 os.mkdir(path)

        moved = 0

        for file in os.listdir(base):
            file_path = os.path.join(base, file)

            if os.path.isfile(file_path):
                _, ext = os.path.splitext(file)

                for folder, extensions in folders.items():
                    if ext.lower() in extensions:
                        shutil.move(file_path, os.path.join(base, folder))
                        moved += 1
                        break

        print(f"Done. {moved} files organized.")       
    elif choice.lower() == "n":
        print("Okay, going back to the main menu...")
    else:
        print("Invalid answer, but going back to main menu anyway due to safety reasons")



while True:
    print("\n=== File utility Tool ===")
    print("1 - Organize Folder")
    print("2 - Bulk rename files")
    print("3 - Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Organizer selected")
        organize_folder()

    elif choice == "2":
        print("Renamer selected")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
