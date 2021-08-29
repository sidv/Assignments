#4.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
lst = []
num = [x for x in input().split(',')]
for bin in num:
    x = int(bin, 2)
    if not x%5:
        lst.append(bin)
print(','.join(lst))