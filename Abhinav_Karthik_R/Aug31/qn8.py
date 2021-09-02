
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def list_diff(lst):
    print(list(set(b).difference(set(lst))))
    
list_diff([int(item) for item in input("Enter the list items : ").split()])
