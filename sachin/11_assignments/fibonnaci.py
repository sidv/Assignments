#4.Write a code to print fibonnaci series( 1,1,2,3,5,8,13,21...) till 100.


First_val = 0
Second_val = 1
for i in range(1,100):
    if(i <= 1):
                next = i
    else:
                next = First_val + Second_val
                First_val = Second_val
                Second_val = next
    print(next)    