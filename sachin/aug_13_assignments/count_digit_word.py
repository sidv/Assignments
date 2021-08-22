#7.Write a program which counts the total letters and digits in the string(take string from user)


string = input("Enter the string : ")

letters_count = 0 
digits_count = 0

lst = string.split(" ")

for i in lst :
    if i.isdigit():
        digits_count = digits_count + 1
    else:
        letters_count = letters_count + 1
print("counts the total digits : " ,digits_count)
print("counts the total letters : " ,letters_count)        


