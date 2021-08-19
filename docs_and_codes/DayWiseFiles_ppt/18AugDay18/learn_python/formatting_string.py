temp = int(input("What's todays temperature"))
humid = int(input("What's todays Humidity"))
name = input("What's your name")

#Greeting
# %Formatting
print("______________% formatting_______________________________")
print("Hello %s!" % name)  #Hello Sid
print("Today's Temperature is %d and humidity is %d" % (temp,humid))

#Format function
print("_____________Format functions_____________________________")
print("Hello {}!".format(name)) #Hello sid!
print("Today's Temperature is {} and Humidity is {}".format(temp,humid))
print("Today's Temperatue is {1} and humidity is {0}".format(temp,humid))
#F string
print("__________________F string______________________________")
print(f"Hello {name}!") #Hello sid!
print(f"Hello {name.upper()}")
print(F"Today's Temperature is {temp} and Humidity is {humid}")
print(f"Today's Temperature is {temp * 100/20} and humidity is {humid * 0.12}")
