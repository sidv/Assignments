#num = int(input(" Enter the number : "))

#print("Multiplication Table of : ")
#for i in range(1,11):
  # print(num,'x',i,'=',num*i)

#print("___________________________________________________________________________________________________________________")


#start = int(input("Enter the start of range: "))
#end = int(input("Enter the end of range: "))

#for num in range(start, end + 1):
 #   if num % 2 == 0:
  #      print(num, end = " ")


#Print("__________________________________________________________________________________________________________")


#start = int(input("Enter the start of range: "))
#end = int(input("Enter the end of range: "))
#for num in range(start, end + 1):
  #  if num % 2 != 0:
   #     print(num, end = " ")



nterms = int(input("How many terms you want? "))

n1 = 0
n2 = 1
count = 2

if nterms <= 0:
   print("Plese enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence:")
   print(n1)
else:
   print("Fibonacci sequence:")
   print(n1,",",n2,end=', ')
   while count < nterms:
       nth = n1 + n2
       print(nth,end=' , ')
       n1 = n2
       n2 = nth
       count += 1





my_str = 'dad'

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


x = "malayalam"
w = ""
for i in x:
    w = i + w
if (x == w):
    print("Yes")
else:
    print("No")




n = float(input("Enter a Number: "))

if n % 7 == 0:

	print(n, "is divisible by 7.")

else:

	print(n, "is not divisible by 7.")







lower = int(input("Enter lower range limit:"))
upper = int(input("Enter upper range limit:"))
for i in range(lower, upper+1):
   if((i%3==0) & (i%5==0)):
      print(i)
