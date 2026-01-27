import csv
import os

def menu():
    print("\n=== CSV FILTER PROGRAM ===")
    print("1 - Preview mode")
    print("2 - Renaming mode")
    print("3 - Quit\n")


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


while True:
    menu()
    choice = input("Choose: ")

    if choice == "1":
        preview_mode()
    elif choice == "2":
        renaming_mode()
    elif choice == "3":
        print("Quitting...")
        break
    else:
        print("Invalid option.")
