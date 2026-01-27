import os
import shutil
import csv

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

def get_int(prompt):
    try:
        return int(input(prompt))
    except:
        print("Invalid number.")
        return None


def get_operator():
    op = input("Operator (>= or <=): ").strip()
    if op in (">=", "<="):
        return op
    print("Invalid operator.")
    return None


def compare(value, threshold, operator):
    if operator == ">=":
        return value >= threshold
    if operator == "<=":
        return value <= threshold


def process_csv(file_name, column_index, threshold, operator, output_name):
    with open(file_name, "r") as infile, open(output_name, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        try:
            header = next(reader)
        except StopIteration:
            print("Empty file.")
            return

        writer.writerow(header)

        for row in reader:
            try:
                value = int(row[column_index])
            except:
                continue

            if compare(value, threshold, operator):
                writer.writerow(row)


def renaming_mode():
    file_name = input("CSV file name (must exist): ")
    if not os.path.exists(file_name):
        print("File not found.")
        return

    column_index = get_int("Column index (0-based): ")
    threshold = get_int("Threshold value: ")
    operator = get_operator()

    if None in (column_index, threshold, operator):
        return

    output_name = "filtered_" + file_name
    process_csv(file_name, column_index, threshold, operator, output_name)
    print("Done. Saved as", output_name)
    input("Press Enter to return to menu")


def preview_mode():
    file_name = input("CSV file name (must exist): ")
    if not os.path.exists(file_name):
        print("File not found.")
        return

    column_index = get_int("Column index (0-based): ")
    threshold = get_int("Threshold value: ")
    operator = get_operator()

    if None in (column_index, threshold, operator):
        return

    output_name = "filtered_preview_" + file_name
    process_csv(file_name, column_index, threshold, operator, output_name)
    print("Done. Saved preview as", output_name)
    input("Press Enter to return to menu")

while True:
    print("\n=== File Utility Tool ===")
    print("1 - Organize Folder")
    print("2 - Bulk rename files")
    print("3 - CSV filter tool (preview mode)")
    print("4 - CSV filter tool (renaming mode)")
    print("5 - Quit")


    choice = input("Choose an option: ")

    if choice == "1":
        organize_folder()

    elif choice == "2":
        bulk_rename()

    elif choice == "3":
        preview_mode()

    elif choice == "4":
        renaming_mode()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
