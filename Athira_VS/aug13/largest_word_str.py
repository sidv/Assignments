s = "A broad range of industrial and consumer products use computers as control systems. Simple special-purpose devices like microwave ovens and remote controls are included, as are factory devices like industrial robots and computer-aided design, as well as general-purpose devices like personal computers and mobile devices like smartphones. Computers power the Internet, which links hundreds of millions of other computers and users. "

wrd_lst = s.split()
#longest_wrd_lst = ""
max_len = 0

for wrd in wrd_lst:
	if len(wrd) > max_len:
		max_len = len(wrd)
		longest_wrd = wrd


print(longest_wrd)
