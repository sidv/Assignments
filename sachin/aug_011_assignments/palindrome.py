#5.Write a code to check the given string is palindrome or not. (abba)


string=input(("Enter the string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")