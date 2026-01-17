import os
import shutil

while True:
	print("Choose an option:\n")
	print("1 - Organize a specific folder(PLEASE PROVIDE THE ABSOLUTE/ENTIRE PATH)\n")
	print("2 - Quit\n") 
	choice = input("")

	if choice == "1":
		base = os.path.expanduser(input("Folder to organize: "))
		base = os.path.abspath(base)

		if not os.path.exists(base):
			print("\nFolder not found:", base)
			continue

		folders = {
			"Images": [".jpg", ".png", ".jpeg"],
			"Documents": [".pdf", ".txt", ".docx"],
			"Videos": [".mp4", ".mov"],
			"Music": [".mp3"],
			"Spreadsheets": [".csv", ".xlsx"]
		}

		for folder in folders:
			path = os.path.join(base, folder)
			os.makedirs(path, exist_ok=True)

		for file in os.listdir(base):
			file_path = os.path.join(base, file)

			if os.path.isfile(file_path):
				_, ext = os.path.splitext(file)

				for folder, extensions in folders.items():
					if ext.lower() in extensions:
						shutil.move(file_path, os.path.join(base, folder))
						
	elif choice == "2":
		print("Quitting...")
		break

	else:
		print("Invalid Option")
