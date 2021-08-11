print('string assignment answers')
head = 'Click Open link on the dialog shown by your browser'
#1.Fetch "browser"
print(head[-7:])
#2.Fetch "link"
print(head[11:16])
#3.Convert Whole string to uppercase
print(head.upper())
#4.Convert whole string to lowercase
print(head.lower())
#5.Convert "Click" to upper case in string
print(head[:5].upper()+head[5:])
#6.Convert "Open" and "browser" to upper case in string
print(head[6:11].upper()+head[11:-7]+head[-7:].upper())
#7.Print "Open link: in reverse order
print(head[14:5:-1])


num="1,2,3,4,5,6,7,8,9"
#8.Print only numbers not comma
print(num[::2])
#9.Print all even numbers
print(num[2::4])
#10.Fetch "1" and "5" from string and perform numerical addition
print(int(num[0])+int(num[8]))

#11.Fetch "2" and "8" from string and perfrom numerical muliplication
print(int(num[2])*int(num[-3]))
