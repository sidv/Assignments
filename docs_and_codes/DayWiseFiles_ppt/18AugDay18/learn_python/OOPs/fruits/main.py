
from fruits import Fruit
#import fruits
fruits = []

while True:
        ch = int(input("Enter your choice: "))
        if ch == 1:
                #add fruit
                id = int(input("Enter fruit id "))
                name = input("Enter fruit name ") 
                rate = int(input("Enter rate "))
                fruits.append(Fruit(id,name,rate))
        elif ch == 2:
                #delete fruit
                id = int(input("Enter fruit id "))
                for i in fruits:
                        if i.id == id:
                                fruits.pop(fruits.index(i))
                                            
        elif ch == 3:
                #display fruit
                for i in fruits:
                        print(f"{i.name} | {i.rate}")
        else:
                print("Invalid choice")




