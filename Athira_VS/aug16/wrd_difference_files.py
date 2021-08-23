with open("data1.txt", "r") as fd1:
	set1 = set(fd1.read().split())
	with open("data2.txt", "r") as fd2:
		set2 = set(fd2.read().split())
		print("\n".join(set1.difference(set2)))

