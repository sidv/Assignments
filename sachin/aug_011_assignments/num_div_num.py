#6.Write a code to check wether a given number is divisible by the given number(Take both number from user)

numa = int(input("Enter a Number numerator: "))

deno = int(input("Enter a Number denominator:"))

if numa%deno==0:
  print(str(numa)+ " is divisible by " +str(deno))
else:
  print(str(numa)+ " is not divisible by " +str(deno))