def create_file(file):
	fd = open(file, "x")
	return fd


def write_to_file(file):
	data = input("Enter data: ")
	with open(file, "w") as fd:
		fd.write(data)


def delete_data(file):
	fd = open(file, "w")
	fd.truncate()
	fd.close()


def read_data(file):
	with open(file, "r") as fd:
		print(fd.read())


def copy_file(file1, file2):
	with open(file1, "r") as fr:
		with open(file2, "w")as fw:
			fw.write(fr.read())


def search_string(file, data):
	with open(file, "r") as fr:
		if data in fr.read():
			print("\tGiven string is present in the file.")


def unique_content(file1, file2):
	with open(file1, "r") as f1:
		with open(file2, "r")as f2:
			set1 = set(f1.read().split())
			set2 = set(f2.read().split())
			print(set1.symmetric_difference(set2))


