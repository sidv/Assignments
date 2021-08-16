
n = int(input("Enter the total no. of Fibonacci numbers to be printed: "))
res = "1"

if n < 0 :
	print("Invalid!! Enter a number greater than 0.")
#if n == 1:
#	print("1")
 
pre = 0
cur = 1
count = 1
while count < n:


	nxt = cur + pre
	res = res + ", "+ str(nxt)
	pre = cur
	cur = nxt

	count += 1

print(res)
