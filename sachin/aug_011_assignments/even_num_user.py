#2.Write a code to print even number using for loop in given range(Take range from user)


start_num = int(input("enter the start range : "))
end_num = int(input("enter the end range : "))

for num in range(start_num, end_num + 1):
      

    if num % 2 == 0:
        print(num)