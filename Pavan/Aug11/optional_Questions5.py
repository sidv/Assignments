print("\n____________Question 5_______________\n")

s=list(input("Enter required string.\n"))
print(s)
x=s.copy()
print(x)
s.reverse()
if x==s:
        print("It is a Palindrome.\n")
else:
        print("No, its not.\n")
