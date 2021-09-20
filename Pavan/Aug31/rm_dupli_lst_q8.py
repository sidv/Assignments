def rm_dupli(lst):
    return(list(set(lst)))

lst = []
for i in range(10):
    lst.append(input("Enter num: "))

print(rm_dupli(lst))
