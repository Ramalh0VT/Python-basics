import os

while True:
	print("Choose an option: \n")
	print("1 - Show the files on a folder \n")
	print("2 - Quit\n")
	option = input("")
	
	if option == "1":
	
		folder = input("Folder(type the entire path):")
		files = ""
		try:
			files = os.listdir(folder)
		except FileNotFoundError:
			print("\nInvalid or nonexistent folder, try again\n")


		count=1
		for file in files:
			file_path = os.path.join(folder, file)
			if os.path.isfile(file_path):
				print(count, file)
				count += 1
	elif option == "2":
		print("Quitting...")
		break

	else:
		print("Invalid option")
