#7.Write a program which counts the total letters and digits in the string(take string from user)

string = input("Enter string: ")

count = 0;  
 
for i in range(0, len(string)):  
    if(string[i] != ' '):  
        count = count + 1;  
   
print("Total number of characters in a string: " + str(count)); 
