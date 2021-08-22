#3.Write a python code to print comma seperated fibinacci numbers(1,1,2,3,5,8,11)(Take limit from user)

limit = int(input("Enter the limit : "))
lst = [1]
First_val = 0
Second_val = 1
for i in range(1,limit):
    if(i <= 1):
                next = i
    else:
                next = First_val + Second_val
                First_val = Second_val
                Second_val = next
                lst.append(next)
print(lst)