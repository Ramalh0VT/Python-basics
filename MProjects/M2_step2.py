import os
while True:
	print("Choose an option: \n")
	print("1 - Rename the files in a folder")
	print("2 - Quit\n")
	choice = input("")

	if choice == "1":

		folder = input("Folder(Please give the whole path): ")

		count = 1
		try:
			for file in os.listdir(folder):
				old_path = os.path.join(folder, file)

				if os.path.isfile(old_path):
					name, ext = os.path.splitext(file)
					new_name = f"file_{count}{ext}"
					new_path = os.path.join(folder, new_name)

					os.rename(old_path, new_path)
					count += 1
		except Exception as e:
			print("Folder not found or invalid folder. Error:", e)
	elif choice == "2":
		print("Quitting...")
		break
	else:
		print("Invalid option")
