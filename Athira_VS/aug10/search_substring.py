var="Click Open link on the dialog shown by your browser"
print(var)
while True:
    sub = input("Enter a substring: ")
    if sub in var:
        print("Substring present")
    else:
        print("Substring not present")
