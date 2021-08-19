print("--------Palindrome---------")
a = "abba"
#Str(input("Enter String: "))
rev = ""
for i in a:
        rev = i + rev
if a == rev:
        print("palindrome")
else:
        print("not palindrome")

print("--------divisible------")
first=int(input("Enter first number: "))
second=int(input("Enter second number: "))
if first / second != 0 :
	print("Divisible")
else:
	print("not Divisible")
