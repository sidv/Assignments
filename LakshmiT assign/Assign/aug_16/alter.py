with open("data1.txt", "r") as fd:
	wrd_lst = fd.read().split()
	with open("data2.txt", "w") as fdw:
		for wrd in wrd_lst[::2]:
			fdw.write(wrd + " ")
