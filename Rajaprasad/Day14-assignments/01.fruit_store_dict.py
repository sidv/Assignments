print('All fruit details')

fruit={}

while True:
    seriel = input("Enter seriel number : ")
    fname = input("Enter fruit name: ")
    rate = input('Ener rate of fruit : ')
    i_from = input('Enter the import source name : ')
    i_date  = input('Enter tha date :')
    buy_price = input('Enter the buying price : ')
    temp = {
        'fruit_name' : fname,
        'rate ' : rate,
        'imported_from' : i_from,
        'imported_date' : i_date,
        'buy_price': buy_price 
    }
    fruit[seriel] = temp
    print(fruit)