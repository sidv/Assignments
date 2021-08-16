
dupl_list = []
s_list = input("Enter the string: ").strip().split()
res = ""


for wrd in s_list:
	if wrd not in dupl_list:
		res = res + " " + wrd
		dupl_list.append(wrd)


print(res)





