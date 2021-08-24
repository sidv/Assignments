#4.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.


lst = [a for a in range(1000,3000) if all(int(b) % 2 == 0 for b in str(a))]
print(lst)

