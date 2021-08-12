str1 = input("Enter a string for palindrome check :")
if str1 == str1[::-1] :

	print(f'{str1} is palinrome')
else:
	print(f'{str1} is not palindrome')
