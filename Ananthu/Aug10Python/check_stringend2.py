string = str(input("Enter any string : "))

print(string[:7:-1])

if string[-1:-4] == "iis":
        print(string," is ending with 'iis'")
else:
        print(string," is not ending with 'iis'")
