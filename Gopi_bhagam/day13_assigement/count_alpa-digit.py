str = input("Enter a alphabet and digits :")
a_count=0 
d_count = 0
for i in str:
    if i.isalpha():
        a_count = a_count+1
    elif i.isdigit():
        d_count =d_count+1
   
print(" total number of aphabets ",a_count)
print("total nuber of  digits ",d_count)
