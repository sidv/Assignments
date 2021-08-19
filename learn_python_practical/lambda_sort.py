lst = [20,303,40,50]
lst.sort()

lst = ["sid","pavan","gopi","ramya","pooja"]
lst.sort() #sort in alphabetical order

lst.sort(key=lambda x: x[-1]) #Sort based on last letter
print(lst)
lst = [[10,20],[60,20],[50,10]]
lst.sort() #Sorts by first index of nested list
lst.sort(key=lambda x: x[1]) #sort based on index 1 of nested list
print(lst)
