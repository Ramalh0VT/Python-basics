import os
import shutil

def organize_folder():
    base = input("Folder to organize (type the whole path): ")

    try:
        if not os.path.exists(base):
            print("Folder not found.")
            return

        choice = input(
            "This will organize files by type. Proceed? (y/N): "
        ).lower()

        if choice != "y":
            print("Going back to menu.")
            return

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

    except Exception as e:
        print("Error:", e)

    input("Press Enter to return to menu")


def bulk_rename():
    folder = input("Type the folder to rename files: ")

    try:
        if not os.path.exists(folder):
            print("Folder not found.")
            return

        base_name = input("Base name (e.g. image, report): ")
        start = int(input("Starting number: "))

        count = start

        # Preview
        for file in os.listdir(folder):
            old_path = os.path.join(folder, file)

            if os.path.isfile(old_path):
                _, ext = os.path.splitext(file)
                new_name = f"{base_name}_{count}{ext}"
                new_path = os.path.join(folder, new_name)
                print(f"{file} -> {new_name}")
                count += 1

        confirm = input("Proceed with these changes? (y/N): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return

        count = start
        renamed = 0

        for file in os.listdir(folder):
            old_path = os.path.join(folder, file)

            if os.path.isfile(old_path):
                _, ext = os.path.splitext(file)
                new_name = f"{base_name}_{count}{ext}"
                new_path = os.path.join(folder, new_name)
                os.rename(old_path, new_path)
                count += 1
                renamed += 1

        print(f"Done. {renamed} files renamed.")

    except Exception as e:
        print("Error:", e)

    input("Press Enter to return to menu")


while True:
    print("\n=== File Utility Tool ===")
    print("1 - Organize Folder")
    print("2 - Bulk rename files")
    print("3 - Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        organize_folder()

    elif choice == "2":
        bulk_rename()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
