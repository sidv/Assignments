print("dictionary in given range")

dic={}
user=int(input("enter range"))
while True:
	for i in range(1,user+1):
		s=i*i
		dict ={ i :s 
		      }
		print(dict)
	break;
