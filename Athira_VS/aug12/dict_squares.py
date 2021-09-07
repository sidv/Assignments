

n =int(input("Enter a  range until which you want to create the squares: "))

square_dict = {}

for i in range(1,n+1):
    square_dict[i] = i*i

print(square_dict)
