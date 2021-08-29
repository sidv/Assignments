lst = [1,2,3,4,5,6,7,8,9,10,24,67]

e_lst = list(filter(lambda a: a%2==0,lst))
print(f"By lambda:  {e_lst}")

#List comprehensions
#[statement]
#[return_variable for_loop ]
#for i in lst:
#	if i%2 == 0:
#	   e_lst.append(i)
print(">>>>>>>>>>>>>>>>")
e_lst = [i for i in lst if i%2 == 0]
print(e_lst)

o_lst = [x for x in lst if x%2 != 0]
print(o_lst)

lst = ["sid","pavan","gopi","RAJA"]
#for i in lst
#	u_lst.append(i.upper())
#
u_lst = [i.upper() for i in lst ]
print(u_lst)

a_lst = [f"{i[0].upper()}{i[1:]}" for i in lst if i[0].islower()]
print(a_lst)

#[i for i in lst]
#true_value if condition else false_value
alt_lst = [i.upper() if i.islower() else i.lower() for i in lst]
print(alt_lst)
#for i in lst:
# 	 i
#
