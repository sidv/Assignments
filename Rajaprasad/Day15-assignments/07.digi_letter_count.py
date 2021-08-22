# print('counting total digit and total letter on the given string')
string = input('enter a string and with containing both letter and digit : ')
digit = 0
letter = 0
for i in string:
    if i.isdigit():
        digit += 1
    else:
        letter += 1
print(f'digits: {digit}\nletters : {letter}')
