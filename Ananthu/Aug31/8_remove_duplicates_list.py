#8.Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

lst = [1,2,3,4,5,1,6,5,4,3,2]
def lst_rem_elm():
    print(list(set(lst)))
lst_rem_elm()    

    
