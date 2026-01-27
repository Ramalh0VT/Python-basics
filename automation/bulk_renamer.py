import os

while True:
    print("Choose an option:\n")
    print("1 - Rename the files in a folder")
    print("2 - Quit\n")
    choice = input("")

    if choice == "1":
        folder = input("Folder (full path): ")

        try:
            base_name = input("Base name (example: image, video): ")
            count = int(input("Starting number: "))
            preview_count = count

            print("\nPreviewing the changes:\n")

            for file in os.listdir(folder):
                old_path_preview = os.path.join(folder, file)

                if os.path.isfile(old_path_preview):
                    name, ext = os.path.splitext(file)
                    new_name_preview = f"{base_name}_{preview_count}{ext}"
                    new_path_preview = os.path.join(folder, new_name_preview)
                    print(f"{file}  →  {new_name_preview}")
                    preview_count += 1

            confirmation = input("\nDo you want to proceed? (y/n): ").lower()

            if confirmation == "y":
                for file in os.listdir(folder):
                    old_path = os.path.join(folder, file)

                    if os.path.isfile(old_path):
                        name, ext = os.path.splitext(file)
                        new_name = f"{base_name}_{count}{ext}"
                        new_path = os.path.join(folder, new_name)
                        os.rename(old_path, new_path)
                        count += 1

                print("\nChanges were made. Returning to main menu.")

            elif confirmation == "n":
                print("\nNo changes made. Returning to main menu.")

            else:
                print("\nInvalid option. Returning to main menu for safety.")

        except Exception as e:
            print("Error:", e)

    elif choice == "2":
        print("Quitting...")
        break

    else:
        print("Invalid option")
