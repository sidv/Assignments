#how to join two strings
fst_name = "SIddhant"
lst_name = "Verma"
full_name = fst_name + lst_name #Use + operator to join string
print(full_name)

full_name = fst_name + " " + lst_name
print(full_name) 

print("______Other test_____________________")
x = 10
y = "20"
a = '30'
b = 40

#z = x + y #Error TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(z)
#z = y + x #Error TypeError: can only concatenate str (not "int") to str
#print(z)

z = y + a #2030
print(z)

z = x + b #Valid it'll perform summation
print(z)
print("____________________________________________")
full_name = "siddhant" "verma" #No Error Its concatonation
print(full_name) 
full_name = fst_name lst_name #SyntaxError  If you are using variable name use + operator else you can " " to perform concatination
print(full_name)
full_name = "siddhant","verma" #No Error it assigns tuple
print(full_name)
