#print('accepts a sequence of comma seperated five numbers and find the addition of all of them')


print('sum of all digits is : ', (sum(int(digit) for digit in input(
    "Enter comma separated sequence of numbers : ").split(','))))
