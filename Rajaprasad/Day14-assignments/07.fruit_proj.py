print('Fruit management system')

f = {}
s_no = 0
f_id = 0
cart = []
while True:
    print("1.-Add fruit \n2.-Delete fruit by name \n3.-Search fruit by name and rate")
    print("4.-Change fruit name and rate")
    print("5.-Add to cart")
    print("6.-Display all fruit data")
    print("7.display cart")
    print('8.exit')

    ch = int(input('Enter choice : '))

    if ch == 1:
        #add fruit
        s_no += 1
        if s_no not in f.keys():
            f_id += 1
            f_name = input("Enter fruit name : ")
            f_rate  = int(input('Enter rate of fruit : '))
            im_from = input('Enter import place of fruit : ')
            im_dt = input('enter import date : ')
            buy_price = float(input('enter buy price like xx.xx : '))
            temp = {
                'fruit_id': f_id,
                'fruit_name' : f_name,
                'Fruit_rate' : f_rate,
                'imported_from' : im_from,
                'imported_date' : im_from,
                'buy_price' : buy_price
            }
            f[s_no] = temp
            print('fruit added successfully')

        else:
            print('serial key already taken')
    elif ch == 2:
        #delete fruit name
        s_no = int(input('enter serial number'))
        if s_no not in f.keys():
            print('wrong serial number')
        else:
            del f[s_no]
    
    elif ch == 3:
        #search fruit by name and rate
        print('a,A => search by name \n b,B => search by rate')
        choice = input('enter choice: ')
        if choice == 'a' or choice == 'A':
            for i in f.values():
                name  = input('Enter fruit name to search : ')
                if i['fruit_name'] == name :
                    print(f" {i['fruit_id']} | {i['fruit_name']} |{i['Fruit_rate']} | {i['imported_from']} |{i['imported_date']} | {i['buy_price']}  ")
                else:
                    print('wrong fruit name ')
        elif choice == 'b' or choice == 'B':
            for v in f.values():
                rate = float(input('provide rate for searching like xx.xx'))
                if v['fruit_rate'] == rate:
                    print(f" {v['fruit_id']} | {v['fruit_name']} |{v['Fruit_rate']} | {v['imported_from']} |{v['imported_date']} | {v['buy_price']}  ")
                else:
                    print('Not available with this price')
    elif ch == 4:
        #change fruit name and rate
        s_no = int(input('Enter serial number : '))
        if s_no not in f.keys():
            print('Please provide right serial number ')
        else:
            print('modify fruit data')
            f[s_no]['fruit_name'] = input('Enter new fruit name :')
            f[s_no]['fruit_rate'] = input('Enter new rate : ')
            print('fruit name modified successfully ')
    elif ch == 5:
        #add to cart
        for i in f.keys():
            print('-'*10)
            print(f'fruit ids :  {i} ')
            print('-'*10)

        print('press on fruit id number to add to cart ')
        cart.append(f[int(input('enter fruit id to add on cart : '))])
        print('Fruit added in the cart successfully')
        
    elif ch == 6:
        #display 
        for i,j in f.items():
            print(f" {i['fruit_id']} | {j['fruit_name']} |{j['Fruit_rate']} | {j['imported_from']} |{j['imported_date']} | {j['buy_price']}  ")
    elif ch == 7:
        print(cart)
    elif ch == 8:
        break
    else: 
        print('Invalid choice')